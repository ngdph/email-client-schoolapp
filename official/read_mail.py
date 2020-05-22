from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from get_mail import getLabels, fetchEmail


def showreadmail(username, password):
    labels = getLabels()
    label_index = 0
    mails = []

    # Get mail
    def fetchMails(fucking_index):
        temp_mails = fetchEmail(labels[fucking_index])["mails"]
        index = 0

        for mail in temp_mails:
            mails.append(mail["subject"])

            mail_subject = ""
            if mail["subject"]:
                mail_subject = mail["subject"]
            else:
                mail_subject = "No subject"

            listMails.insert(index, mail_subject)
            index += 1

    # Get mail subjects from label
    def viewSubjectsByLabel(event):
        label_index = listLabels.curselection()[0]
        print(listLabels.curselection()[0])
        fetchMails(listLabels.curselection()[0])

    def SlcBack():
        import option

        ReadMail.destroy()
        option.showoption(username, password)

    ReadMail = Tk()
    ReadMail.title("Đọc Mail")
    ReadMail.geometry("700x400")
    ReadMail.resizable(0, 0)

    lbLabels = Label(ReadMail, text="Labels")
    lbLabels.place(x=10, y=10)

    listLabels = Listbox(ReadMail, selectborderwidth=7, font=("Times New Roman", 12))
    listLabels.place(x=10, y=30)

    lb_index = 0
    for lb in labels:
        print(lb, type(lb))
        listLabels.insert(lb_index, f"{lb}")
        lb_index += 1

    listLabels.bind("<Double-Button-1>", viewSubjectsByLabel)

    lbMails = Label(ReadMail, text="Mails")
    lbMails.place(x=60, y=10)

    listMails = Listbox(
        ReadMail, selectborderwidth=6, font=("Times New Roman", 12), width=55
    )
    listMails.place(x=210, y=30)


# showreadmail("18520165@gm.uit.edu.vn", "1634608674")
