from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from get_mail import getLabels, fetchEmail


def showreadmail(username, password):
    label_index = 0

    def fetchMails():
        listMail = Listbox(ReadMail)

    def jumpViewMail(event):
        label_index = listLabels.curselection()[0]

        print(listLabels.get(label_index))

    def SlcBack():
        import option

        ReadMail.destroy()
        option.showoption(username, password)

    ReadMail = Tk()
    ReadMail.title("Đọc Mail")
    ReadMail.geometry("700x400")

    lbLabels = Label(ReadMail, text="Labels")
    lbLabels.place(x=10, y=10)

    labels = getLabels()

    listLabels = Listbox(ReadMail, selectborderwidth=7, font=("Times New Roman", 12))
    listLabels.place(x=10, y=30)

    for (index, label) in enumerate(labels):
        listLabels.insert(index, f"{label}")

    listLabels.bind("<Double-Button-1>", jumpViewMail)

    lbMails = Label(ReadMail, text="Mails")
    lbMails.place(x=60, y=10)


# showreadmail("18520165@gm.uit.edu.vn", "1634608674")
