from tkinter import *
from tkinter.ttk import *
import imaplib
from imap_tools.mailbox import MailBox


def moving_dialog(username, password, init_label, labels, mail_id):
    root = Tk()
    root.title("Copy to...")
    root.geometry("300x120")
    root.resizable(0, 0)

    label_list = Combobox(root, state="readonly")
    label_list.place(x=20, y=30, width=260, height=20)

    def init_listbox():
        if isinstance(labels, list):
            if len(labels) > 0:
                label_list["values"] = tuple(labels)

    def on_accept():

        # try:
        print(mail_id)
        imap_client = imaplib.IMAP4_SSL("imap.gmail.com")
        imap_client.login(username, password)

        imap_client.select(f'"{init_label}"')

        status, response = imap_client.uid("COPY", mail_id, f'"{label_list.get()}"')

        # if status == "OK":
        #     imap_client.select(f'"{init_label}"')
        #     imap_client.store(mail_id, "+X-GM-LABELS", "\\Trash")
        #     imap_client.expunge()
        #     # imap_client.move(mail_id.decode(),)

        root.destroy()
        return True

        # except Exception as e:
        #     print(e)
        #     root.destroy()
        #     return False

    def on_cancel():
        root.destroy()
        return False

    button_accept = Button(root, text="Accept", command=on_accept)
    button_accept.place(x=30, y=70, width=100, height=24)

    button_cancel = Button(root, text="Cancel", command=on_cancel)
    button_cancel.place(x=170, y=70, width=100, height=24)

    init_listbox()

#     root.mainloop()


# moving_dialog("f", "f", "f", "f", "f")

