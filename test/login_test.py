from tkinter import *
from tkinter import messagebox
import webbrowser
import smtplib

import info

# user = None
# password = None
# receiver = None

user = info.UserInformation()


def login(username, passwords):
    # global user, password
    # user1 = user
    # password1 = password
    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, passwords)
        print(77777)
        return True
    except Exception as e:
        print(e)
        return False


def Login_Gmail(username, password):
    user.setUsername(username)
    user.setPassword(password)

    obj = login(user.getUsername(), user.getPassword())
    if obj is not False:
        messagebox.showinfo("Thông báo", "Đăng nhập thành công")
    # except Exception as e:
    else:
        messagebox.showerror("Thông báo", "Đăng nhập thất bại")


def browser_createAccount(url):
    webbrowser.open_new(url)


def Display_About():
    messagebox.showinfo(
        "About my application",
        "Nhóm 9:\nNgày bắt đầu đồ án: 13/4/2020\nThis app is for only educational purpose\nCreated by: Psy Squad-Uit\nNon-Copywrite\nPhiên bản: 7.0.x",
    )


def Show_Login():
    login = Tk()

    # Tên cửa sổ
    login.title("Login")
    # Kích thước cửa sổ
    login.geometry("500x200")

    # Label "Username"
    lb_username = Label(login, text="Username: ")
    lb_username.place(x=100, y=10)

    # Label "Password"
    lb_password = Label(login, text="Password: ")
    lb_password.place(x=100, y=50)

    # textbox "Username"
    txb_username = Entry(login, width=30)
    txb_username.place(x=250, y=10, width=200)

    # textbox "Password"
    txb_password = Entry(login, width=30, show="*")
    txb_password.place(x=250, y=50, width=200)

    # Lưu lại giá trị của username, password vào biến user, password.
    # def get_data():
    #     global user, password
    #     user = txb_username.get()
    #     password = txb_password.get()

    #     print(user)
    #     print(password)

    # button Login
    btn_Login = Button(
        login,
        text="Login",
        command=lambda: Login_Gmail(txb_username.get(), txb_password.get()),
    )
    btn_Login.place(x=200, y=100)

    # label "warning"
    lb_warning = Label(
        login, text="Please turn on less secure app on Gmail before login", fg="red"
    )
    lb_warning.place(x=100, y=130)

    # label Tạo tài khoản
    lb_createAccount = Label(login, text="Chưa có tài khoản? Đăng ký")
    lb_createAccount.place(x=150, y=150)

    # hyperlink tạo account
    hpl_createAccount = Label(login, text="tại đây", fg="blue", cursor="hand2")
    hpl_createAccount.place(x=300, y=150)
    hpl_createAccount.bind(
        "<Button-1>",
        lambda e: browser_createAccount(
            "https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"
        ),
    )

    # menu About
    menu_About = Menu(login)
    menu_About.add_command(label="About", command=Display_About)
    login.config(menu=menu_About)

    login.mainloop()


Show_Login()
