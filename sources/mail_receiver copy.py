import email
import imaplib
import quopri
import base64
import re


from email import header


SERVER = "imap.gmail.com"
# EMAIL = "nguyen.dphux@gmail.com"
# PASSWORD = "Ilovesex123*"

# Đăng nhập vào server


def get_labels(username, password):

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username, password)

    # Khởi tạo label rỗng
    TOTAL_LABELS = 0
    LABELS = []

    # Lấy hết tất cả label
    RAW_LABELS = mail.list()[1]
    TOTAL_LABELS = len(mail.list()[1])

    # mail.list() trả về 1 tuple có 2 phần tử
    # Example: ('OK', [b'(\\HasNoChildren) "/" "INBOX"', b'(\\HasChildren \\Noselect) "/" "[Gmail]"',
    # b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"', b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Bin"',
    # b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"', b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"',
    # b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"', b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"',
    # b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"'])
    # Phần tử thứ 1 là trạng thái, thứ 2 là list các label dưới dạng byte
    # => Phải bytes.decode từng phần tử trong list để lấy được chuỗi
    # => Lọc ra label thích hợp và append vào list
    # Example: ['INBOX', '[Gmail]', '[Gmail]/All Mail', '[Gmail]/Bin', '[Gmail]/Drafts', '[Gmail]/Important', '[Gmail]/Sent Mail', '[Gmail]/Spam', '[Gmail]/Starred']

    # đưa label vào list
    for i in range(0, TOTAL_LABELS):
        # LABEL là 1 chuỗi đã qua xử lý với đoạn regex để lấy được phần label
        LABEL = re.findall('"([^"]*)"', bytes.decode(RAW_LABELS[i], "utf-8"))[-1]

        # re.findall sẽ trả về list ['/', 'INBOX'] với INBOX là tên label tương ứng với chuỗi xử lý, vì ở cuối nên ta để index là [-1] để lấy phần tử cuối
        LABELS.append(LABEL)

    return LABELS[2:]


def get_emails_id(username, password, label):

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username, password)

    mail.select(f'"{label}"')

    status, data = mail.search(None, "ALL")

    mails = {"label": "", "mails": []}
    mails["label"] = label

    mail_ids = []

    for block in data:
        mail_ids = block.split()

    return mail_ids


def get_emails(username, password, label):

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username, password)

    # Chọn label cần lấy mail
    # f là để truyền biến vào chuỗi qua {}
    mail.select(f'"{label}"')

    # Tìm kiếm tất cả mail trong hộp thư theo LABEL
    # Search trả về 1 tuple với 2 phần tử là trạng thái và list chứa 1 phần tử là dãy byte chứa id của mail
    # Search nhận 2 tham số là charset (từ khoá tìm kiếm) và criteria (chuẩn tìm kiếm)
    # Tham khảo https://gist.github.com/martinrusev/6121028
    # Dưới đây search(None, 'ALL') là không tìm theo từ khoá và chọn tất cả mail trong label
    status, data = mail.search(None, "ALL")

    mails = {"label": "", "mails": []}
    mails["label"] = label

    mail_ids = []

    # data là list chỉ chứa 1 phần tử là 1 dãy byte là các id của mail nên vòng for cũng chỉ là duyệt 1 vòng
    # block.split() là để trả về list chứa từng phẩn tử của dãy byte đó
    # => mail_ids += block.split() không khác gì mail_ids = block.split(), chỉ là gán list chứa phần tử cho list rỗng
    for block in data:
        mail_ids = block.split()

    # return
    # Duyệt qua từng id của mail và lấy mail về, đồng thời xử lý mail đó
    for i in mail_ids[:7]:
        # fetch trả về tuple 2 phần tử là status và list các response được trả về từ server
        # Gán data là reponse được trả về từ server
        status, data = mail.fetch(i, "(RFC822)")

        # Khởi tạo dictionary chứa dữ liệu mail rỗng
        mail_data = {"from": None, "subject": None, "content": []}
        # Duyệt qua các thành phần của mail
        for response_part in data:

            # Khởi tạo dict chứa dữ liệu content của mail
            # contentType: kiểu dữ liệu (chuỗi)
            # encodeType: kiểu encode (chuỗi)
            # payload: dữ liệu (chuỗi hoặc byte)
            # filename: tên file của phần file đính kèm(nếu có) (chuỗi), nếu chỉ là phần nội dung mail thì phần này sẽ là None
            data_part = None

            # Nếu dữ liệu là tuple thì xét tiếp vì có chứa dữ liệu
            if isinstance(response_part, tuple):

                # Lấy From và Subject của mail
                # response_part chứa 2 phần tử là định dạng của mail và byte dữ liệu nên ta chọn [1]
                message = email.message_from_bytes(response_part[1])
                print(type(message))

                # Lấy người gửi
                mail_data["from"] = message["From"]

                # Lấy người nhận
                mail_data["to"] = message["To"]

                # Decode subject của mail
                # Lấy tiêu đề, vì tiêu đề cũng có thể viết bằng nhiều ngôn ngữ nên phải được decode
                if message["Subject"]:
                    # decode_header trả về list với 2 phần tử là tiêu đề và kiểu encode nên ta chọn [0]
                    mail_data["subject"], encoding = header.decode_header(
                        message["Subject"]
                    )[0]

                    if message["CryptKey"]:
                        mail_data["cryptKey"] = message["CryptKey"]

                    # Nếu tiêu đề trả về là dạng bytes thì phải decode ra
                    if isinstance(mail_data["subject"], bytes):
                        mail_data["subject"] = mail_data["subject"].decode("utf-8")
                else:
                    # Trường hợp tiêu đề rỗng
                    mail_data["subject"] = ""

                # Lấy payload của mail
                # payload chứa nội dung, file đính kèm, v.v....
                # Nội dung, file... đều được tách riêng trong payload nên ta phải duyệt qua để xử lý
                mail_content = message.get_payload()

                # Nếu payload của email có nhiều phần
                if message.is_multipart():
                    # Duyệt qua từng phần của nội dung mail
                    for data in mail_content:

                        decoded = data.get_payload(decode=True)
                        # Decode payload của các phần
                        # Ở đây xử lý để payload nếu là chuỗi thì trả về string, nếu là base64 sẽ trả về hex dưới dạng byte

                        # if (data['Content-Transfer-Encoding'] == 'quoted-printable'):
                        #     decoded = quopri.decodestring(
                        #         data.get_payload().encode()).decode('utf-8')

                        # if (data['Content-Transfer-Encoding'] == 'base64'):
                        #     decoded = data.get_payload(decode=True)

                        # Gán các giá trị vào dict
                        data_part["contentType"] = data.get_content_type()
                        data_part["encodeType"] = data["Content-Transfer-Encoding"]
                        data_part["filename"] = data.get_filename()
                        data_part["payload"] = decoded

                        filename = ""

                        if data_part["filename"]:
                            filename = data_part["filename"].split("\\")[-1]
                        else:
                            filename = None

                        # print(filename.split("\\")[-1])

                        # with open(filename.split("\\")[-1], "wb") as f:
                        #     f.write(decoded)

                        # Append vào list dữ liệu của mail
                        mail_data["content"].append(data_part)

                        # Reset lại dict
                        data_part = {
                            "contentType": None,
                            "encodeType": None,
                            "payload": None,
                            "filename": None,
                        }

                # Nếu payload email chỉ có 1 phần
                else:
                    # Gán các giá trị vào dict
                    data_part["contentType"] = message.get_content_type()
                    data_part["encodeType"] = message["Content-Transfer-Encoding"]
                    data_part["payload"] = message.get_payload()
                    # Append vào list dữ liệu của mail
                    mail_data["content"].append(data_part)

        # Append vào danh sách mail
        mails["mails"].append(mail_data)

    # Trả về danh sách mail
    # print(mails)
    return mails


labels = get_labels("18520165@gm.uit.edu.vn", "1634608674")
print(labels, type(labels))
get_emails("18520165@gm.uit.edu.vn", "1634608674", "[Gmail]/Starred")
