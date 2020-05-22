from tkinter import *
from tkinterhtml import HtmlFrame
import re


# from read_mail import showreadmail


def view_mail(mail):
    email_from = re.search("<(.*)>", mail["from"]).group(1)
    email_to = ""
    email_content = None

    print(mail)
    read_selected_mail = Tk()
    read_selected_mail.title(mail["subject"])
    read_selected_mail.geometry("700x400")
    read_selected_mail.resizable(0, 0)

    # Listbox Labels navigation
    lbFrom = Label(read_selected_mail, text=f"From: {email_from}")
    lbFrom.place(x=10, y=10)

    for content in mail["content"]:
        if "text" in content["contentType"]:
            email_content = content["payload"]

    # textPayload = Text(read_selected_mail)
    # textPayload.insert(INSERT, email_content.decode(), CHAR)
    # textPayload.place(x=10, y=30)

    frame = HtmlFrame(read_selected_mail, horizontal_scrollbar="auto")

    frame.set_content(email_content.decode())
    frame.place(x=10, y=30)
