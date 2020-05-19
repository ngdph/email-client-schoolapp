import smtplib, email
import base64
import os
from tkinter import messagebox
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from AES import *

# from email import encoders


def Send_mail_with_attachment(
    username, password, receiver_email="", Subject="", message="", list_file=[],
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
                messagebox.showinfo("Thong bao", "Da gui!")
                server.quit()

        # Khong co message va file
        else:
            messagebox.showerror("Sai roi th ngu", "Khong co noi dung!")

    # Khong co nguoi nhan
    else:
        messagebox.showerror("Sai roi th ngu", "Nhap nguoi nhan di!")
