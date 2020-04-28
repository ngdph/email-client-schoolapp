import smtplib, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp.gmail.com"

sender_email = "nhanth240500@gmail.com"
receiver_email = "18520326@gm.uit.edu.vn"
password = "@177687Nhan@"

msg = MIMEMultipart()

#msg = MIMEMultipart("alternative"); #Dùng khi gửi theo dạng html

#Thông tin về From, To, Subject, Bcc của mail.
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Gui Nhan."
msg["Bcc"] = receiver_email

	#Message của người gửi muốn người nhận nhận được
body_mail = """\
Hello Nhan,
Dao nay m khoe khong?
Facebook cua tao ne
Hen m toi nay 8h nhe!
Good bye."""

	#Định dạng message của mail theo kiểu plain text và lưu vào message_mail
message_mail = MIMEText(body_mail, "plain") 
	#part2 = MIMEText(html, "html")

	#Đính kèm nội dung mail đang được lưu trong par1 vào msg
msg.attach(message_mail)
	#msg.attach(part2)

filename = "listmails.txt"  # In same directory as script

	# Open PDF file in binary mode
with open(filename, "rb") as attachment:
		# Add file as application/octet-stream
		# Email client can usually download this automatically as attachment
	file_mail = MIMEBase("application", "octet-stream")
	file_mail.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
encoders.encode_base64(file_mail)

	# Add header as key/value pair to attachment part
file_mail.add_header(
	"Content-Disposition",
	f"attachment; filename= {filename}",
)

msg.attach(file_mail)
all_message = msg.as_string()

try:
		#Tạo một đối tượng SMTP, cho phép kết nối tới server của SMTP và cho phép sử dụng các phương thức của SMTP
	server = smtplib.SMTP(smtp_server, port)

		#Tạo kết nối SMTP không bảo mật và mã hóa nó với starttls()
	server.starttls()

		#Đăng nhập tài khoản gmail của người gửi
	server.login(sender_email, password)

		#Tiến hành gửi mail từ người gửi tới người nhận, message được định dang theo string.
	server.sendmail(sender_email, receiver_email, all_message)
	
	#Trong trường hợp có lỗi khi kết nối tới server của SMTP hoặc xảy ra bất kì lỗi gì trong quá trình xử lí
	#Sẽ xuất thông báo lỗi
except Exception as e:
	print(e)

finally:
	server.quit()
