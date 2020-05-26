from tkinter import *
from tkinter.ttk import Combobox
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
    #GUI_mail_reader.resizable(0, 0)

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

    text_message = Text(GUI_mail_reader, width=84, height=20)
    text_message.insert(INSERT, email_content.decode(), CHAR)
    text_message.configure(state="disabled")
    text_message.place(x=10, y=30)

    label_type_crypto = Label(GUI_mail_reader, text="Type cryptography:")
    label_type_crypto.place(x=10, y=365)

    combobox_select_crypto = Combobox(
        GUI_mail_reader,
        values=["None", "Caesar", "Vigenere", "AES", "RSA"],
        width=30,
        state="readonly",
        height=1
    )
    combobox_select_crypto.current(0)
    combobox_select_crypto.place(x=150, y=368)

    def event_pressed_decrypt():
        pass

    button_decrypt = Button(GUI_mail_reader,height=1, text="Decrypt", command=event_pressed_decrypt)
    button_decrypt.place(x=370, y=365)
    def event_pressed_reply():
         from mail_sender import display_send_mail
         display_send_mail("18520165@gm.uit.edu.vn", "1634608674")
    def event_pressed_foward():
        pass
    button_reply = Button(GUI_mail_reader,height=1, text="Reply",command=event_pressed_reply)
    button_reply.place(x=570, y=365)

    button_forward = Button(GUI_mail_reader,height=1, text="Forward", command=event_pressed_foward)
    button_forward.place(x=630, y=365)
    # frame = HtmlFrame(GUI_mail_reader, horizontal_scrollbar="auto")

    # frame.set_content(email_content.decode())
    # frame.place(x=10, y=30)
