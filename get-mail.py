import email
import imaplib
import quopri
import base64
import re


from email import header


SERVER = 'imap.gmail.com'
EMAIL = "nhanth240500@gmail.com"
PASSWORD = "@177687Nhan@"

# Đăng nhập vào server
mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)


def getLabels():
    # Khởi tạo label rỗng
    TOTAL_LABELS = 0
    LABELS = []

    # Lấy hết tất cả label
    TOTAL_LABELS = len(mail.list()[1])

    # đưa label vào list
    for i in range(0, TOTAL_LABELS):
        LABEL = re.findall(
            '"([^"]*)"', bytes.decode(mail.list()[1][i], 'utf-8'))[-1]
        LABELS.append(LABEL)

    return LABELS


def fetchEmail(label):

    # Chọn label cần lấy mail
    mail.select(f'"{label}"')
    # Tìm kiếm tất cả mail trong hộp thư theo LABEL
    status, data = mail.search(None, 'ALL')

    mails = {
        'label': '',
        'mails': []
    }
    mail_ids = []

    # Lấy mail id
    for block in data:
        mail_ids += block.split()

    # Duyệt qua từng id của mail và lấy mail về
    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')

        # Khởi tạo dictionary chứa dữ liệu mail rỗng
        mail_data = {
            'from': None,
            'subject': None,
            'content': []
        }

        # Duyệt qua các thành phần của mail
        for response_part in data:

            # Khởi tạo dict chứa dữ liệu content của mail
            data_part = {
                "contentType": None,
                "encodeType": None,
                "payload": None,
                "filename": None
            }

            # Nếu dữ liệu là tuple thì xét
            if isinstance(response_part, tuple):

                # Lấy From và Subject của mail
                message = email.message_from_bytes(response_part[1])
                mail_data['from'] = message['From']

                # Decode subject của mail
                if (message['Subject']):
                    mail_data['subject'], encoding = header.decode_header(message['Subject'])[0]
                    if isinstance(mail_data['subject'], bytes):
                        mail_data['subject'] = mail_data['subject'].decode(
                            "utf-8")
                else:
                    mail_data['subject'] = ''

                print(mail_data['subject'])

                # Lấy payload của mail
                mail_content = message.get_payload()

                # Nếu payload của email có nhiều phần
                if message.is_multipart():
                    for data in mail_content:

                        # Decode payload của các phần
                        decoded = ''
                        if (data['Content-Transfer-Encoding'] == 'quoted-printable'):
                            decoded = quopri.decodestring(
                                data.get_payload().encode()).decode('utf-8')

                        else:
                            decoded = data.get_payload(decode=True)

                        # Gán các giá trị vào dict
                        data_part['contentType'] = data.get_content_type()
                        data_part['encodeType'] = data['Content-Transfer-Encoding']
                        data_part['filename'] = data.get_filename()
                        data_part['payload'] = decoded

                        # Append vào list dữ liệu của mail
                        mail_data['content'].append(data_part)

                        # Reset lại dict
                        data_part = {
                            "contentType": None,
                            "encodeType": None,
                            "payload": None,
                            "filename": None
                        }

                # Nếu payload email chỉ có 1 phần
                else:
                    # Gán các giá trị vào dict
                    data_part['contentType'] = message.get_content_type()
                    data_part['encodeType'] = message['Content-Transfer-Encoding']
                    data_part['payload'] = message.get_payload()

                    # Append vào list dữ liệu của mail
                    mail_data['content'].append(data_part)

        # Append vào danh sách mail
        mails['mails'].append(mail_data)

    # Trả về danh sách mail
    # print(mails)
    return mails


labels = getLabels()
fetchEmail(labels[-1])
