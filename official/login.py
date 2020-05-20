from tkinter import *
import webbrowser
from tkinter import Menu
from tkinter import messagebox
from option import showoption


# IDtxt = "none"
# Passtxt = "none"


class Email:
    def __init__(self, username, password, cl):
        self._username = username
        self._password = password
        self._email = username
        self.client = {"Gmail": ["smtp.gmail.com", 587]}
        import smtplib

        self.email_client = self.client[cl][0]
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


# tạo ô about
def About():
    messagebox.showinfo(
        "About",
        "Nhóm 9:\nNgày bắt đầu đồ án: 13/4/2020\nThis app is for only educational purpose\nCreated by Psy Squad-Uit\nNon-Copywrite\nPhiên bản: 7.0.x",
    )


class authenticate:
    def __init__(self, Login):
        # form login
        Login.geometry("500x200")
        Login.title("Login")

        # menubar about
        """self.about = Menu(Login)
        self.about.add_command(label="About", command=About)
        Login.config(menu=about)"""

        # tạo và place Label ID và pass
        self.senderID = Label(Login, text="Gmail ID: ", font=("Arial", 10))
        self.senderPass = Label(Login, text="Gmail Pass: ", font=("Arial", 10))
        self.senderID.place(x=100, y=10)
        self.senderPass.place(x=100, y=50)

        # tạo ô nhập ID
        self.IDtxt = Entry(Login)

        # tạo ô nhập pass
        self.Passtxt = Entry(Login, show="*")

        # place ô ID và Pass
        self.IDtxt.place(x=250, y=10, width=200)
        self.Passtxt.place(x=250, y=50, width=200)

        # make connection toi Gmail
        self.LoginBtn = Button(Login, text="Đăng nhập", command=self.make_connection)
        self.LoginBtn.place(x=200, y=100)

        # label please turn on less secure app on Gmail before login
        self.trn = Label(
            Login, text="please turn on less secure app on Gmail before login", fg="red"
        )
        self.trn.place(x=100, y=130)

        def browser_Warning(url):
            webbrowser.open_new(url)

        self.hyperlink_Warning = Label(Login, text="at here", fg="blue", cursor="hand2")
        self.hyperlink_Warning.place(x=349, y=130)
        self.hyperlink_Warning.bind(
            "<Button-1>",
            lambda e: browser_Warning(
                "https://myaccount.google.com/u/0/lesssecureapps?pli=1"
            ),
        )
        # label để đăng ký
        self.signin = Label(Login, text="Chưa có tài khoản? Đăng ký")
        self.signin.place(x=150, y=150)
        # lấy hyper link
        def browser_SignUp(url):
            webbrowser.open_new(url)

        self.hyperlink_SignUp = Label(Login, text="tại đây", fg="blue", cursor="hand2")
        self.hyperlink_SignUp.place(x=300, y=150)
        self.hyperlink_SignUp.bind(
            "<Button-1>",
            lambda e: browser_SignUp(
                "https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"
            ),
        )
        self.Login = Login

    def make_connection(self):

        user = self.IDtxt.get()
        password = self.Passtxt.get()
        client = "Gmail"
        connect = Email("nguyen.dphux@gmail.com", "Ilovesex123*", client)
        # print(client, user, password)
        x = connect.login()
        # connect.event()
        if x is not False:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công")
            self.Login.destroy()
            showoption(user, password)
        else:
            messagebox.showerror(
                "Connection Fail, try again", "Tài khoản hoặc mật khẩu không hợp lệ"
            )


if __name__ == "__main__":
    root = Tk()
    auth = authenticate(root)
    root.mainloop()
