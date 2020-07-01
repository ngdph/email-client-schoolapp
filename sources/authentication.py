from tkinter import *
import webbrowser
from tkinter import Menu
from tkinter import messagebox
from navigation import display_navigation


class Email:
    def __init__(self, account_id, account_password):
        self.username = account_id
        self.password = account_password

        import smtplib
        import imaplib

        self.smtp = smtplib.SMTP("smtp.gmail.com", 587)
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")

    def login(self):
        try:
            self.smtp.connection("smtp.gmail.com", 587)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.login(self.username, self.password)

            self.imap.login(self.username, self.password)

            return True
        except:
            return False


# tạo ô about
def display_pressed_about():
    messagebox.showinfo(
        "About",
        "Group 8:\Starting date: 13/4/2020\nThis app is only for educational purposes\nDeveloped by Psy Squad - UIT\nNon-copyrighted\nv0.7.0.1",
    )


def display_pressed_Feedback():
    messagebox.showinfo(
        "Send feedback",
        "Have feedback? We'd love to hear it, but please don't share sensitive information. Have questions or legal concerns? Try help or support at A14_PSY_SQUAD@gmail.com",
    )


class Authenticate:
    def __init__(self, GUI_login):
        # form login
        GUI_login.geometry("500x200")
        GUI_login.resizable(0, 0)
        GUI_login.title("Authentication")

        # tạo và place Label ID và pass
        self.label_account_id = Label(GUI_login, text="Gmail ID: ", font=("Arial", 10))
        self.label_account_id.place(x=100, y=10)

        menu_about = Menu(GUI_login)
        menu_about.add_command(label="About", command=display_pressed_about)
        menu_about.add_command(label="Feedback", command=display_pressed_Feedback)

        GUI_login.config(menu=menu_about)

        self.label_account_password = Label(
            GUI_login, text="Gmail Password: ", font=("Arial", 10)
        )
        self.label_account_password.place(x=100, y=50)

        self.entry_account_id = Entry(GUI_login)
        self.entry_account_id.focus()
        self.entry_account_id.place(x=250, y=10, width=200)

        self.entry_account_password = Entry(GUI_login, show="*")
        self.entry_account_password.place(x=250, y=50, width=200)

        # make connection toi Gmail
        self.button_login = Button(GUI_login, text="Log In", command=self.connection)
        self.button_login.place(x=200, y=100)

        # label please turn on less secure app on Gmail before login
        self.label_warning = Label(
            GUI_login,
            text="Please turn on less secure app on Gmail before login",
            fg="red",
        )
        self.label_warning.place(x=100, y=130)

        def browser_warning(url):
            webbrowser.open_new(url)

        self.hyperlink_warning = Label(
            GUI_login, text="at here", fg="blue", cursor="hand2"
        )
        self.hyperlink_warning.place(x=349, y=130)
        self.hyperlink_warning.bind(
            "<Button-1>",
            lambda e: browser_warning(
                "https://myaccount.google.com/u/0/lesssecureapps?pli=1"
            ),
        )
        # label để đăng ký
        self.label_signin = Label(GUI_login, text="Don't have account? Sign up")
        self.label_signin.place(x=150, y=150)

        def browser_signup(url):
            webbrowser.open_new(url)

        self.hyperlink_signup = Label(
            GUI_login, text="at here", fg="blue", cursor="hand2"
        )
        self.hyperlink_signup.place(x=305, y=150)
        self.hyperlink_signup.bind(
            "<Button-1>",
            lambda e: browser_signup(
                "https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"
            ),
        )
        self.GUI_login = GUI_login

    def connection(self):

        username = self.entry_account_id.get()
        password = self.entry_account_password.get()
        connection = Email(username, password)
        login_status = connection.login()

        if login_status:
            self.GUI_login.destroy()
            display_navigation(username, password, connection)
        else:
            messagebox.showerror(
                "Could not connection, please try again",
                "Username or password is invalid.",
            )


if __name__ == "__main__":
    root = Tk()
    auth = Authenticate(root)
    root.mainloop()
