from tkinter import *
from tkinter.ttk import Combobox, Treeview, Scrollbar
import re
import os
import base64
import cgi

from crypt_box import decrypt_func
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import cryptor


def read_mail_func(username, password, mail):
    email_to = ""
    email_content = ""
    email_signature = ""
    email_signature_key = ""
    html_content = ""
    email_attachments = []
    subject = mail["header"]["Subject"]

    if "From" in mail["header"]:
        try:
            email_from = mail["header"]["From"].decode()
        except:
            email_from = mail["header"]["From"]

    if "from" in mail["header"]:
        try:
            email_from = mail["header"]["from"].decode()
        except:
            email_from = mail["header"]["from"]

    GUI_mail_reader = Tk()
    GUI_mail_reader.title(
        mail["header"]["Subject"].decode()
        if mail["header"]["Subject"] and isinstance(mail["header"]["Subject"], bytes)
        else mail["header"]["Subject"]
        if mail["header"]["Subject"] and isinstance(mail["header"]["Subject"], str)
        else "(No subject)"
    )
    GUI_mail_reader.geometry("720x600")
    GUI_mail_reader.resizable(0, 0)

    # Listbox Labels navigation
    label_sender = Label(GUI_mail_reader, text=f"From: {email_from}")
    label_sender.place(x=20, y=10)

    def event_pressed_decrypt():
        decrypt_func(email_content, email_signature, email_signature_key)

    def event_pressed_save():
        for file in email_attachments:
            path = os.path.join("C:/Users", os.getlogin(), "Downloads", "Mailex")
            os.makedirs(path, exist_ok=True)
            f = open(os.path.join(path, file["filename"]), "wb")
            f.write(file["payload"]["payload"])
            f.close()

    button_decrypt = Button(
        GUI_mail_reader, height=1, text="Decrypt", command=event_pressed_decrypt
    )
    button_decrypt.place(x=120, y=565)

    button_decrypt = Button(
        GUI_mail_reader, height=1, text="Save all files", command=event_pressed_save
    )
    button_decrypt.place(x=20, y=565)

    def event_pressed_reply():
        from mail_replier import display_reply_mail

        display_reply_mail(
            username, password, subject, email_from, email_content.decode()
        )

    def event_pressed_foward():
        from mail_forwarder import display_forward_mail

        display_forward_mail(
            username,
            password,
            subject,
            email_from,
            [email_to if email_to else ""],
            email_content.decode(),
        )

    button_reply = Button(
        GUI_mail_reader, height=1, text="Reply", command=event_pressed_reply
    )
    button_reply.place(x=570, y=565)

    button_forward = Button(
        GUI_mail_reader, height=1, text="Forward", command=event_pressed_foward
    )
    button_forward.place(x=630, y=565)

    treeview = Treeview(GUI_mail_reader, height=8)
    treeview.place(x=20, y=370)

    vertical_scrollbar = Scrollbar(
        GUI_mail_reader, orient="vertical", command=treeview.yview
    )
    vertical_scrollbar.place(x=680, y=370)

    treeview.configure(xscrollcommand=vertical_scrollbar.set)
    treeview["columns"] = ("File", "Verified")
    treeview["show"] = "headings"

    treeview.column("File", width=320, anchor="c")
    treeview.column("Verified", width=320, anchor="c")

    treeview.heading("File", text="File")
    treeview.heading("Verified", text="Verified status")

    for content in mail["payload"]:
        file_index = 0

        if "text/plain" in content["header"]["Content-Type"]:
            email_content = content["payload"]

        if "Signature" in content["header"]:
            email_signature = content["header"]["Signature"]

        if "Signature-Verifier" in content["header"]:
            email_signature_key = content["header"]["Signature-Verifier"]

        if "Content-Disposition" in content["header"]:
            value, params = cgi.parse_header(content["header"]["Content-Disposition"])

            if "filename" in params or "filename*" in params:

                filename = ""

                if "filename" in params:
                    filename = params["filename"]

                if "filename*" in params:
                    filename = params["filename*"].split("''")[1]

                file_index += 1
                attachment = {
                    "filename": filename,
                    "payload": content,
                    "verified": "Verified",
                }

                if "Signature" in content["header"]:
                    try:
                        signature = bytes.fromhex(content["header"]["Signature"])
                        pub = RSA.import_key(
                            bytes.fromhex(content["header"]["Signature-Verifier"])
                        )
                        public_key = pkcs1_15.new(pub)

                        file_data = content["payload"]

                        hashed_f = SHA256.new()
                        hashed_f.update(file_data)

                        public_key.verify(hashed_f, signature)
                        attachment["verified"] = "Valid"

                    except Exception as e:
                        print(e)
                        attachment["verified"] = "Invalid"

                else:
                    attachment["verified"] = "No signature found"

                treeview.insert(
                    "",
                    "end",
                    text=file_index,
                    values=(attachment["filename"], attachment["verified"]),
                )
                email_attachments.append(attachment)

    if not email_content:
        email_content = b"Not supported yet"

    text_message = Text(GUI_mail_reader, wrap="word", width=84, height=20)
    text_message.configure(state=NORMAL)
    text_message.insert(INSERT, email_content.decode(), CHAR)
    text_message.configure(state=DISABLED)
    text_message.place(x=20, y=30)

    GUI_mail_reader.mainloop()

