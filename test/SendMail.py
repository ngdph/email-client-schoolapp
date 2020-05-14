from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from sendmailwithattach import Send_mail_with_attachment


def showsendmail(username, password):
    def SlcBack():
        SendMail.destroy()
        import option

        option.showoption(username, password)

    SendMail = Tk()
    SendMail.title("Gửi Mail")
    SendMail.geometry("400x300")

    def event():
        Send_mail_with_attachment(
            username,
            password,
            EntTo.get(),
            EntSubject.get(),
            EntMessage.get(),
            filepaths.get().split(", "),
        )

    #### Nhóm "Mail người nhận"
    # Label "To"
    lblTo = Label(SendMail, text="To:")
    lblTo.place(x=50, y=10)
    # Entry "To"
    EntTo = Entry(SendMail)
    EntTo.place(x=100, y=10, width=200)

    #### Nhóm "Subject"
    # Label "Subject"
    lblSubject = Label(SendMail, text="Subject:")
    lblSubject.place(x=50, y=35)
    # Entry "Subject"
    EntSubject = Entry(SendMail)
    EntSubject.place(x=100, y=35, width=200)

    ### Nhóm "message"
    # Label "message"
    lbl_Message = Label(SendMail, text="Message:")
    lbl_Message.place(x=48, y=70)
    # Entry "Message"
    EntMessage = Entry(SendMail)
    EntMessage.place(x=100, y=70, width=200, height=150)

    ###nhóm "chọn file"
    ###event "chọn file"
    def slcFile():
        file_path = filedialog.askopenfilenames(parent=SendMail, title="Choose a file")
        filepaths.configure(state=NORMAL)
        filepaths.insert(0, ", ".join(file_path))

    # button "chọn file"
    btn_file = Button(SendMail, text="Gủi file", command=slcFile)
    btn_file.place(x=80, y=260)
    filepaths = Entry(SendMail, state=DISABLED)
    filepaths.place(x=10, y=240)

    # Button send
    btnSend = Button(SendMail, text="Send", command=event)
    btnSend.place(x=150, y=260)

    ### button để quay lại tab option
    btnBack = Button(SendMail, text="Back", command=SlcBack)
    btnBack.place(x=300, y=260)
    SendMail.mainloop()


showsendmail("18520165@gm.uit.edu.vn", "1634608674")
