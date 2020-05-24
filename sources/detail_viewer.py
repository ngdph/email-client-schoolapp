from tkinter import *
import re


# from read_mail import showreadmail


def read_mail_func(mail):
    try:
        email_from = re.search("<(.*)>", mail["from"]).group(1)
    except:
        email_from = mail["from"]

    email_to = ""
    email_content = None

    # print(mail)
    GUI_mail_reader = Tk()
    GUI_mail_reader.title(mail["subject"])
    GUI_mail_reader.geometry("700x400")
    GUI_mail_reader.resizable(0, 0)

    # Listbox Labels navigation
    label_sender = Label(GUI_mail_reader, text=f"From: {email_from}")
    label_sender.place(x=10, y=10)

    for content in mail["content"]:
        if content["contentType"] == "text/plain":
            email_content = content["payload"]

        # if content["contentType"] == "application/octet-stream":
        #     file =
    if not email_content:
        email_content = b"Not supported yet"

    text_message = Text(GUI_mail_reader)
    text_message.insert(INSERT, email_content.decode(), CHAR)
    text_message.configure(state="disabled")
    text_message.place(x=10, y=30)

    # frame = HtmlFrame(GUI_mail_reader, horizontal_scrollbar="auto")

    # frame.set_content(email_content.decode())
    # frame.place(x=10, y=30)
