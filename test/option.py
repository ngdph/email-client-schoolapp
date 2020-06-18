from tkinter import *

#chuyển qua tab soạn mail
def SlcSend():
	Option.destroy()
	import sendmail
#chuyển qua tab đọc mail
def SlcRead():
	pass
###button Log out
def clickedLogout():	
	Option.destroy()
	import login	

#tạo form option	
Option= Tk()
Option.title("Option")
Option.geometry("300x200")

#button soan mail
WriteMail = Button(Option,text="Soạn mail",command=SlcSend)
WriteMail.place(x=5,y=10,width=290)

#Label chú thích soạn mail
lbWrite = Label(Option,text="Dùng SMTP để gửi mail, có hỗ trợ attachment.")
lbWrite.place(x=5,y=40) 

#button đọc mail
ReadMail = Button(Option, text="Đọc mail",command=SlcRead)
ReadMail.place(x=5,y=80,width=290)

#Label chú thích đọc mail
lbRead = Label(Option,text="Dùng IMAP4 để đọc mail.")
lbRead.place(x=5,y=110) 

#button Logout quay lại tab Login	
Logout = Button (Option,text="Logout",command=clickedLogout)
Logout.place(x=240,y=160)
Option.mainloop()
