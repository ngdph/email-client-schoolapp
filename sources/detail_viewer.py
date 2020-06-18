from tkinter import *
from tkinter.ttk import Combobox
import re
import os
import base64
import threading

# from cefpython3 import cefpython as cef
import sys
import html_viewer
from crypt_box import decrypt_func


def read_mail_func(username, password, mail):
    email_to = None
    email_content = None
    html_content = None
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
    GUI_mail_reader.geometry("700x400")
    GUI_mail_reader.resizable(0, 0)

    def html_to_data_uri(html=""):
        html = html.encode("utf-8", "replace")
        b64 = base64.b64encode(html).decode("utf-8", "replace")
        ret = "data:text/html;base64,{data}".format(data=b64)
        return ret

        # cef.Shutdown()

    # Listbox Labels navigation
    label_sender = Label(GUI_mail_reader, text=f"From: {email_from}")
    label_sender.place(x=10, y=10)

    for content in mail["content"]:
        if content["contentType"] == "text/plain":
            email_content = content["payload"].decode()

        if content["contentType"] == "text/html":
            html_content = html_to_data_uri(content["payload"].decode())

        if content["filename"]:
            path = os.path.join("C:/Users", os.getlogin(), "Downloads", "Mailex")
            os.makedirs(path, exist_ok=True)
            file = open(os.path.join(path, content["filename"]), "wb")
            file.write(content["payload"])
            file.close()

    if not email_content:
        email_content = b"Not supported yet"

    text_message = Text(GUI_mail_reader, wrap="word", width=84, height=20)
    text_message.insert(INSERT, email_content, CHAR)
    text_message.configure(state="disabled")
    text_message.place(x=10, y=30)

    def event_pressed_decrypt():
        decrypt_func(
            email_content, mail["cryptKey"] if hasattr(mail, "cryptKey") else None
        )

    button_decrypt = Button(
        GUI_mail_reader, height=1, text="Decrypt", command=event_pressed_decrypt
    )
    button_decrypt.place(x=370, y=365)

    def event_pressed_reply():
        from mail_replier import display_reply_mail

        display_reply_mail(
            username, password, subject, email_from, email_content,
        )

    def event_pressed_foward():
        from mail_forwarder import display_forward_mail

        display_forward_mail(
            username,
            password,
            subject,
            email_from,
            [email_to if email_to else ""],
            email_content,
        )

    button_reply = Button(
        GUI_mail_reader, height=1, text="Reply", command=event_pressed_reply
    )
    button_reply.place(x=570, y=365)

    button_forward = Button(
        GUI_mail_reader, height=1, text="Forward", command=event_pressed_foward
    )
    button_forward.place(x=630, y=365)

    # html_viewer.init(html_content)

    # def on_closing():
    #     print("closing")
    #     GUI_mail_reader.destroy()

    # chromiumFrame = Frame(GUI_mail_reader, height=800, width=600)
    # chromiumFrame.pack(side="top", fill="x")

    # def display_chromium(frame):
    #     sys.excepthook = cef.ExceptHook
    #     # window_info = cef.WindowInfo(frame.winfo_id())
    #     # window_info.SetAsChild(frame.winfo_id(), [0, 0, 800, 200])
    #     cef.Initialize()
    #     # browser = cef.CreateBrowserSync(
    #     #      url=html_content, window_title=str(subject)
    #     # )
    #     # cef.MessageLoop()

    # thread = threading.Thread(target=display_chromium, args=(chromiumFrame))
    # thread.start()

    # # GUI_mail_reader.protocol("WM_DELETE_WINDOW", on_closing)
    # # GUI_mail_reader.mainloop()
