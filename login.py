from tkinter import *
import webbrowser
from tkinter import Menu
from tkinter import messagebox


class Email():
    def __init__(self, username, password, cl):
        self._username = username
        self._password = password
        self._email = username
        self.client = {'Gmail':['smtp.gmail.com', 587]}
        import smtplib
        self.email_client=self.client[cl][0]
        self.port = self.client[cl][1]
        self.smtp = smtplib.SMTP(self.email_client, self.port)
        self.cl = cl
    def login(self):
        try:
            self.smtp.connect(self.email_client, self.port)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.login(self._username, self._password)
            return True
##            from imaplib import IMAP4_SSL
##            self.imap = IMAP4_SSL('outlook.office365.com', 993)
##            self.imap.login(self._email, self._password)
##            print('IMAP Connection Successful')
        except:
            return False


#form login
Login = Tk()
Login.geometry('500x200')
Login.title("Login")

#khai báo biến cho ID và pass
send_email=StringVar()
send_pass=StringVar()

#tạo ô about
def About():
    messagebox.showinfo("About", "Nhóm 9:\nNgày bắt đầu đồ án: 13/4/2020\nThis app is for only educational purpose\nCreated by Psy Squad-Uit\nNon-Copywrite\nPhiên bản: 7.0.x") 
about=Menu(Login)
about.add_command(label="About",command=About)
Login.config(menu=about)


#tạo và place Label ID và pass
senderID = Label(Login, text = "Gmail ID: ", font=("Arial",10))
senderPass = Label(Login, text = "Gmail Pass: ", font=("Arial",10))
senderID.place(x=100,y=10)
senderPass.place(x=100,y=50)

#tạo place holder và chỗ nhập ID
IDtxt =Entry(Login,textvariable=send_email)
IDtxt.insert(0, "Mail người gửi")
IDtxt.configure(state=DISABLED)
def on_click_id(event):
    IDtxt.configure(state=NORMAL)
    IDtxt.delete(0, END)
    # ko bị mất khi bấm lại
    IDtxt.unbind('<Button-1>', on_click_ID)
on_click_ID = IDtxt.bind('<Button-1>', on_click_id)

#tạo place holder và chỗ nhập pass
Passtxt = Entry(Login) 
Passtxt.insert(0,"Mật khẩu mail")
Passtxt.configure(state=DISABLED)
def on_click_ps(event):
    Passtxt2 = Entry(Login, textvariable = send_pass,show="*")
    Passtxt2.place(x=250,y=50,width=200)
    Passtxt2.focus()
    # ko bị mất khi bấm lại
    Passtxt.unbind('<Button-1>', on_click_pass)
on_click_pass = Passtxt.bind('<Button-1>', on_click_ps)

#place ô ID và Pass
IDtxt.place(x=250,y=10,width=200)
Passtxt.place(x=250,y=50,width=200)




#make connection toi Gmail
def make_connection():
        
            user = send_email.get()
            password = send_pass.get()
            client = 'Gmail'
            connect = Email(user, password, client)
            
            x = connect.login()
            if x is not False:
                messagebox.showinfo("Thông báo","Đăng nhập thành công") 
                Login.destroy()
                import option
            else:
                messagebox.showerror('Connection Fail, try again',\
                                           "Tài khoản hoặc mật khẩu không hợp lệ")


#tạo button Login
LoginBtn = Button(Login,text="Đăng nhập",command=make_connection)
LoginBtn.place(x=200,y=100)


#label please turn on less secure app on Gmail before login
trn = Label(Login, text="please turn on less secure app on Gmail before login",fg ="red")
trn.place(x=100,y=130)

#label để đăng ký
signin = Label(Login, text="Chưa có tài khoản? Đăng ký")
signin.place(x=150,y=150)
#lấy hyper link
def callback(url):
    webbrowser.open_new(url)
hyperlink = Label(Login, text="tại đây", fg="blue", cursor="hand2")
hyperlink.place(x=300,y=150)
hyperlink.bind("<Button-1>", lambda e: callback("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"))

Login.mainloop()