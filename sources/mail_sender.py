from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib, email, base64, os

from AES import *
from Caesar import *


def display_send_mail(username, password, list_reciever=None):
    GUI_send_mail = Tk()
    GUI_send_mail.title("Gửi Mail")
    GUI_send_mail.geometry("500x400")

    def event_pressed_back():
        GUI_send_mail.destroy()
        import navigation

        navigation.display_navigation(username, password)

    def event_pressed_send():
        send_mail_func(
            username,
            password,
            entry_to.get(),
            entry_subject.get(),
            entry_message.get(0.0, END),
            filepaths.get().split(", "),
            combobox_select_crypto.get(),
        )

    #### Nhóm "Mail người nhận"
    # Label "To"
    label_to = Label(GUI_send_mail, text="To:")
    label_to.place(x=50, y=10)
    # Entry "To"
    entry_to = Entry(GUI_send_mail)
    entry_to.place(x=150, y=10, width=200)

    #### Nhóm "Subject"
    # Label "Subject"
    label_subject = Label(GUI_send_mail, text="Subject:")
    label_subject.place(x=50, y=35)
    # Entry "Subject"
    entry_subject = Entry(GUI_send_mail)
    entry_subject.place(x=150, y=35, width=200)

    ### Nhóm "message"
    # Label "message"
    label_message = Label(GUI_send_mail, text="Message:")
    label_message.place(x=48, y=70)
    # Entry "Message"
    entry_message = Text(GUI_send_mail)
    entry_message.place(x=150, y=70, width=200, height=150)

    # Option Encryption
    label_type_crypto = Label(GUI_send_mail, text="Type crypto:")
    label_type_crypto.place(x=50, y=280)

    combobox_select_crypto = Combobox(
        GUI_send_mail,
        values=["None", "Caesar", "Vigenere", "AES", "RSA"],
        width=30,
        state="readonly",
    )
    combobox_select_crypto.current(0)
    combobox_select_crypto.place(x=150, y=280)
    ###nhóm "chọn file"
    ###event_pressed_send "chọn file"
    def event_select_file():
        file_path = filedialog.askopenfilenames(
            parent=GUI_send_mail, title="Choose a file"
        )
        filepaths.configure(state=NORMAL)
        filepaths.insert(0, ", ".join(file_path))
        filepaths.configure(state=DISABLED)

    # button "chọn file"
    button_file = Button(GUI_send_mail, text="Select file", command=event_select_file)
    button_file.place(x=350, y=320)
    filepaths = Entry(GUI_send_mail, width=30, state=DISABLED)
    filepaths.place(x=150, y=320)

    # Button send
    button_send = Button(GUI_send_mail, text="Send", command=event_pressed_send)
    button_send.place(x=200, y=350)

    ### button để quay lại tab navigation
    button_back = Button(GUI_send_mail, text="Back", command=event_pressed_back)
    button_back.place(x=380, y=350)
    # GUI_send_mail.mainloop()


# display_send_mail("18520165@gm.uit.edu.vn", "1634608674")


def send_mail_func(
    username,
    password,
    receiver_email="",
    Subject="",
    message="",
    list_file=[],
    crypto_type=None,
):
    port = 587
    smtp_server = "smtp.gmail.com"

    # Neu khong co nguoi nhan
    if receiver_email != "":

        # Neu message khong rong hoac co file dinh kem
        if message != "" or list_file[0] != "":
            bbc = receiver_email
            msg = MIMEMultipart()

            # msg = MIMEMultipart("alternative"); #Dùng khi gửi theo dạng html

            # Thông tin về From, To, Subject, Bcc của mail.
            msg["From"] = username
            msg["To"] = receiver_email
            msg["Subject"] = Subject
            msg["Bcc"] = bbc

            print("send mail")

            # Neu message khong rong
            if message != "":
                # Message của người gửi muốn người nhận nhận được
                body_mail = message
                print(body_mail)

                if crypto_type == "AES":
                    body_mail = AES_Encrypt(
                        body_mail, "0123456789abcdef", "0123456789abcdef"
                    )
                elif crypto_type == "Caesar":
                    body_mail = Caesar_Encrypt(body_mail, 13)[: len(body_mail) - 1]
                # body_mail = cryptor.

                # Định dạng message của mail theo kiểu plain text và lưu vào message_mail
                message_mail = MIMEText(body_mail, "plain", "utf-8")
                # part2 = MIMEText(html, "html")

                # Đính kèm nội dung mail đang được lưu trong par1 vào msg
                msg.attach(message_mail)

            # Neu co file dinh kem
            if list_file[0] != "":
                attachments = list_file  # In same directory as script
                # sau khi print ra thì filepath bị split mỗi kí tự thành 1 phần tử của list => sai
                # cần fix lỗi chỗ này.

                for i in range(0, len(attachments)):
                    file = attachments[i]
                    file_basename = os.path.basename(file)
                    # Open PDF file in binary mode
                    with open(file, "rb") as attachment:
                        # Add file as application/octet-stream
                        # Email client can usually download this automatically as attachment
                        file_mail = MIMEBase("application", "octet-stream")
                        file_mail.set_payload(attachment.read())

                    # Encode file in ASCII characters to send by email
                    encoders.encode_base64(file_mail)

                    # Add header as key/value pair to attachment part
                    file_mail.add_header(
                        "Content-Disposition",
                        "attachment",
                        filename=("utf-8", "", file_basename),
                    )
                    msg.attach(file_mail)

            all_message = msg.as_string()

            try:
                # Tạo một đối tượng SMTP, cho phép kết nối tới server của SMTP và cho phép sử dụng các phương thức của SMTP
                server = smtplib.SMTP(smtp_server, port)

                # Tạo kết nối SMTP không bảo mật và mã hóa nó với starttls()
                server.starttls()

                # Đăng nhập tài khoản gmail của người gửi
                server.login(username, password)

                # Tiến hành gửi mail từ người gửi tới người nhận, message được định dang theo string.
                server.sendmail(username, receiver_email, all_message)

                # Trong trường hợp có lỗi khi kết nối tới server của SMTP hoặc xảy ra bất kì lỗi gì trong quá trình xử lí
                # Sẽ xuất thông báo lỗi
            except Exception as e:

                print(e)

            finally:
                messagebox.showinfo("Success", "Sent!")
                server.quit()

        # Khong co message va file
        else:
            messagebox.showerror("Error", "The content is empty!")

    # Khong co nguoi nhan
    else:
        messagebox.showerror("Error", "Please specify at least one recipient.!")
