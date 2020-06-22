from tkinter import *
from tkinter.ttk import Combobox, Treeview, Scrollbar
import re
import os
import base64
import threading

# from cefpython3 import cefpython as cef
import sys
from crypt_box import decrypt_func
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import cryptor


def read_mail_func(username, password, mail):
    email_to = None
    email_content = None
    email_signature_key = None
    html_content = None
    email_attachments = []
    subject = mail["subject"]

    def html_to_data_uri(html):
        html = html.encode("utf-8", "replace")
        b64 = base64.b64encode(html).decode("utf-8", "replace")
        ret = b"data:text/html;base64,{data}".format(data=b64)

        return ret

    try:
        email_from = re.search("<(.*)>", mail["from"]).group(1)
    except:
        email_from = mail["from"]

    GUI_mail_reader = Tk()
    GUI_mail_reader.title(mail["subject"])
    GUI_mail_reader.geometry("720x600")
    GUI_mail_reader.resizable(0, 0)

    def html_to_data_uri(html=""):
        html = html.encode("utf-8", "replace")
        b64 = base64.b64encode(html).decode("utf-8", "replace")
        ret = "data:text/html;base64,{data}".format(data=b64)
        return ret

        # cef.Shutdown()

    # Listbox Labels navigation
    label_sender = Label(GUI_mail_reader, text=f"From: {email_from}")
    label_sender.place(x=20, y=10)

    def event_pressed_decrypt():
        decrypt_func(email_content.decode(), email_signature_key)

    def event_pressed_save():
        for file in email_attachments:
            path = os.path.join("C:/Users", os.getlogin(), "Downloads", "Mailex")
            os.makedirs(path, exist_ok=True)
            f = open(os.path.join(path, file["content"]["filename"]), "wb")
            f.write(file["content"]["payload"])
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

    for content in mail["content"]:
        file_index = 0
        if content["contentType"] == "text/plain":
            email_content = content["payload"]

        if content["contentType"] == "text/html":
            html_content = html_to_data_uri(content["payload"].decode())

        if content["Signature-Verifier"]:
            email_signature_key = content["Signature-Verifier"]
            email_content = email_content[:-512]

        if content["filename"]:
            file_index += 1
            attachment = {"content": content, "verified": "Verified"}

            print(content["Signature"])

            if content["Signature"]:
                try:
                    signature = bytes.fromhex(content["Signature"])
                    pub = RSA.import_key(bytes.fromhex(content["Signature-Verifier"]))
                    public_key = pkcs1_15.new(pub)

                    file = content["payload"]

                    hashed_f = SHA256.new()
                    hashed_f.update(file)

                    public_key.verify(hashed_f, signature)
                    attachment["verified"] = "Valid"

                except Exception as e:
                    print(e)
                    attachment["verified"] = "Invalid"

            else:
                attachment["verified"] = "No signature"

            treeview.insert(
                "",
                "end",
                text=file_index,
                values=(content["filename"], attachment["verified"]),
            )
            email_attachments.append(attachment)

    if not email_content:
        email_content = b"Not supported yet"

    text_message = Text(GUI_mail_reader, wrap="word", width=84, height=20)
    text_message.configure(state=NORMAL)
    text_message.insert(INSERT, email_content.decode(), CHAR)
    text_message.configure(state=DISABLED)
    text_message.place(x=20, y=30)

    # GUI_mail_reader.mainloop()
