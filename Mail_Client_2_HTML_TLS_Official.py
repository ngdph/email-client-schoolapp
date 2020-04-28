import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp.gmail.com"

sender_email = "nhanth240500@gmail.com"
receiver_email = "18520326@gm.uit.edu.vn"
password = input("Type your password and press enter: ")

def Send_Mail():
	msg = MIMEMultipart(); 

	#msg = MIMEMultipart("alternative"); #Dùng khi gửi theo dạng html

	#Thông tin về From, To, Subject, Bcc của mail.
	msg["From"] = sender_email
	msg["To"] = receiver_email
	msg["Subject"] = "Gui Nhan."
	msg["Bcc"] = receiver_email

	#Message của người gửi muốn người nhận nhận được
	text = """\
	Hello Nhan,
	Dao nay m khoe khong?
	Facebook cua tao ne
	Hen m toi nay 8h nhe!
	Good bye."""

	'''html = """\
	<html>
		<body>
			<p>
				Hello Nhan,<br>
				Dao nay m khoe khong?<br>
				<a href = "https://www.facebook.com/hoanggnhann/"> Facebook cua tao ne </a>
			</p>
		</body>
	</html>
	"""'''

	#Định dạng message của mail theo kiểu plain text và lưu vào part1
	part1 = MIMEText(text, "plain") 
	#part2 = MIMEText(html, "html")

	#Đính kèm nội dung mail đang được lưu trong par1 vào msg
	msg.attach(part1)
	#msg.attach(part2)

	try:
		#Dùng smtp để kết nối với smtp server theo giao thức TLS
		#Trong 
		server = smtplib.SMTP(smtp_server, port)
		server.starttls()
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, msg.as_string())
	except Exception as e:
		print(e)
	finally:
		server.quit()