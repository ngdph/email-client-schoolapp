from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from get_mail import getLabels, fetchEmail
from view_detail import view_mail


def showreadmail(username, password):
    labels = getLabels()
    label_index = 0
    selected_mail_index = 0
    mails = []

    # Get mail
    def fetchMails(index_of_label):
        temp_mails = fetchEmail(labels[index_of_label])["mails"]
        index = 0

        # Append mail subject to list box subject
        for mail in temp_mails:
            mails.append(mail)

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

    # Back button
    def SlcBack():
        import option

        ReadMail.destroy()
        option.showoption(username, password)

    def viewEmail(event):
        selected_mail_index = listMails.curselection()[0]
        view_mail(mails[selected_mail_index])

    # instance of tk
    ReadMail = Tk()
    ReadMail.title("Đọc Mail")
    ReadMail.geometry("700x400")
    ReadMail.resizable(0, 0)

    # Listbox Labels navigation
    lbLabels = Label(ReadMail, text="Labels")
    lbLabels.place(x=10, y=10)

    listLabels = Listbox(ReadMail, selectborderwidth=7, font=("Times New Roman", 12))
    listLabels.place(x=10, y=30)

    # interate labels loop and insert it to listLabels
    lb_index = 0
    for lb in labels:
        print(lb, type(lb))
        listLabels.insert(lb_index, f"{lb}")
        lb_index += 1

    listLabels.bind("<Double-Button-1>", viewSubjectsByLabel)

    # info label Listbox
    lbMails = Label(ReadMail, text="Mails")
    lbMails.place(x=60, y=10)

    # Listbox subject
    listMails = Listbox(
        ReadMail, selectborderwidth=6, font=("Times New Roman", 12), width=55
    )
    listMails.place(x=210, y=30)

    # Bind view mail function to mail subject
    listMails.bind("<Double-Button-1>", viewEmail)
