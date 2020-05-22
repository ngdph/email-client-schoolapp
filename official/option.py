from tkinter import *
from SendMail import showsendmail
from read_mail import showreadmail


def showoption(username, password):
    # tạo form option
    Option = Tk()
    Option.title("Option")
    Option.geometry("300x500")
    Option.geometry("300x200")

    #####

    # chuyển qua tab soạn mail
    def SlcSend():
        Option.destroy()
        showsendmail(username, password)

    # button soan mail
    WriteMail = Button(Option, text="Send Mail", command=SlcSend)
    WriteMail.place(x=5, y=10, width=290)

    # Label chú thích soạn mail
    lbWrite = Label(Option, text="Dùng SMTP để gửi mail, có hỗ trợ attachment.")
    lbWrite.place(x=5, y=40)

    # chuyển qua tab đọc mail
    def SlcRead():
        Option.destroy()
        showreadmail("nguyen.dphux@gmail.com", "Ilovesex123*")

    # button đọc mail
    ReadMail = Button(Option, text="Đọc mail", command=SlcRead)
    ReadMail.place(x=5, y=80, width=290)

    # Label chú thích đọc mail
    lbRead = Label(Option, text="Dùng IMAP4 để đọc mail.")
    lbRead.place(x=5, y=110)

    ###button Log out
    # event logout
    def clickedLogout():
        Option.destroy()
        import login

        root = Tk()
        auth = login.authenticate(root)
        # root.mainloop()

    # button Logout quay lại tab Login
    Logout = Button(Option, text="Logout", command=clickedLogout)
    Logout.place(x=1, y=1)
    Logout.place(x=240, y=160)

    Option.mainloop()


showoption("18520165@gm.uit.edu.vn", "1634608674")
