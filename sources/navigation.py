from tkinter import *


from mail_manager import display_read_mail
from mail_sender import display_send_mail


def display_navigation(username, password, connection):
    # tạo form option
    GUI_navigation = Tk()
    GUI_navigation.title("Navigation")
    GUI_navigation.geometry("300x200")
    GUI_navigation.resizable(0, 0)

    # chuyển qua tab soạn mail
    def event_pressed_send():
        GUI_navigation.destroy()
        display_send_mail(username, password)

    # button soan mail
    button_compose = Button(
        GUI_navigation, text="Send mail", command=event_pressed_send
    )
    button_compose.place(x=5, y=10, width=290)

    # Label chú thích soạn mail
    label_depict_sendmail = Label(
        GUI_navigation, text="Using SMTP for sending email, attachment files."
    )
    label_depict_sendmail.place(x=5, y=40)

    # chuyển qua tab đọc mail
    def event_pressed_read():
        GUI_navigation.destroy()
        display_read_mail(username, password)

    # button đọc mail
    button_read = Button(GUI_navigation, text="Manage mail", command=event_pressed_read)
    button_read.place(x=5, y=80, width=290)

    # Label chú thích đọc mail
    label_depict_readmail = Label(
        GUI_navigation, text="Using IMAP4 for receiving and reading mail."
    )
    label_depict_readmail.place(x=5, y=110)

    ###button Log out
    # event signout
    def event_pressed_signout():
        GUI_navigation.destroy()
        import authentication

        root = Tk()
        auth = authentication.Authenticate(root)
        root.mainloop()

    # button button_signout quay lại tab Login
    button_signout = Button(
        GUI_navigation, text="Sign out", command=event_pressed_signout
    )
    button_signout.place(x=1, y=1)
    button_signout.place(x=240, y=160)


# display_navigation("nguyen.dphux@gmail.com", ".*")
