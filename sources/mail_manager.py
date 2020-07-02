from tkinter import *
from tkinter import simpledialog
from mail_receiver import *
from detail_viewer import read_mail_func
import threading
from imapclient import IMAPClient
import pyisemail

# from future.moves.tkinter import simpledialog

label_index = 0


def display_read_mail(username, password):
    # instance of tk
    GUI_read_mail = Tk()
    GUI_read_mail.title("Manage mail")
    GUI_read_mail.geometry("700x430")
    GUI_read_mail.resizable(0, 0)

    mail_labels = get_labels(username, password)
    selected_mail_index = 0
    mails = []
    mails_ids = []

    # Get mail
    def fetch_subjects_func(index_of_label):
        # Xác định label
        # Lấy mail từ label
        # get_mails trả về dict chứa label và mails
        # Lấy value trong key mails
        temp_mails = get_emails(username, password, mail_labels[index_of_label])[
            "mails"
        ]
        temp_mails_ids = get_emails_id(username, password, mail_labels[index_of_label])
        mail_index = 0

        # Xoá hết mail khi chọn label mới
        # mails.clear()
        # mails_ids.clear()

        mails_ids = temp_mails_ids
        # Append mail subject to list box subject
        for index, mail in enumerate(temp_mails):
            mails.append(mail)

            mail_subject = ""
            if mail["subject"]:
                mail_subject = mail["subject"]
            else:
                mail_subject = "No subject"

            listbox_subject_mails.insert(
                mail_index, (mail_subject, temp_mails_ids[index])
            )
            mail_index += 1

    def something():
        mail_labels

    def create_mailbox():
        mailbox_name = simpledialog.askstring(
            "New mailbox", "Mailbox name:", parent=GUI_read_mail
        )

        if mailbox_name:
            imap_client = imaplib.IMAP4_SSL("imap.gmail.com")
            imap_client.login(username, password)
            imap_client.create(mailbox_name)

            listbox_labels_gmail.delete(0, END)
            mail_labels = get_labels(username, password)
            lb_index = 0
            for lb in mail_labels:
                listbox_labels_gmail.insert(lb_index, f"{lb}")
                lb_index += 1

    def delete_mailbox():
        labels = mail_labels
        mailbox_name = labels[listbox_labels_gmail.curselection()[0]]

        if isinstance(mailbox_name, str):
            imap_client = imaplib.IMAP4_SSL("imap.gmail.com")
            imap_client.login(username, password)
            imap_client.delete(mailbox_name)

            listbox_labels_gmail.delete(0, END)

            labels = get_labels(username, password)
            lb_index = 0
            for lb in labels:
                listbox_labels_gmail.insert(lb_index, f"{lb}")
                lb_index += 1

    # Get mail subjects from label
    def extract_subjects_by_label_func(event):
        global label_index
        listbox_subject_mails.delete(0, "end")
        label_index = listbox_labels_gmail.curselection()[0]
        fetch_subjects_func(listbox_labels_gmail.curselection()[0])

    # Back button
    def event_pressed_back():
        import navigation

        GUI_read_mail.destroy()
        navigation.display_navigation(username, password)

    def event_pressed_delete():
        import imaplib
        import ssl

        global label_index
        index = listbox_subject_mails.curselection()[0]
        mail_id = listbox_subject_mails.get(index)[1]

        imap_client = imaplib.IMAP4_SSL("imap.gmail.com")
        imap_client.login(username, password)

        imap_client.select(f'"{mail_labels[label_index]}"')

        imap_client.store(mail_id, "X-GM-LABELS", "\\Trash")
        imap_client.expunge()

    def view_mail_func(event):
        read_mail_func(
            username, password, mails[listbox_subject_mails.curselection()[0]]
        )

    def event_search():
        if entry_search.get():
            if entry_search.get().strip():
                query = [word for word in entry_search.get().split(" ") if word.strip()]

                if len(query) == 3:
                    if (
                        (
                            query[0] == "FROM"
                            or query[0] == "TO"
                            or query[0] == "SUBJECT"
                        )
                        and query[1] == ":"
                        and (
                            (pyisemail.is_email(query[2]) and query[0] != "SUBJECT")
                            or (query[2].strip() and query[0] == "SUBJECT")
                        )
                    ):

                        search_string = (
                            r'(X-GM-RAW "subject:\"' + query[2] + '"")'
                            if query[0] == "SUBJECT"
                            else "(" + query[0] + ' "' + query[2] + '")'
                        )

                        pass

    def on_close():
        threads = threading.enumerate()

        # for thread in threads:
        #     thread._stop.

    # Listbox Labels navigation
    # label_gmail = Label(GUI_read_mail, text="Labels")
    # label_gmail.place(x=10, y=10)

    # compose_search = Button(GUI_read_mail, text="Send mail")
    # compose_search.place(x=45, y=15, width=100, height=30)

    entry_search = Entry(GUI_read_mail, width=60)
    entry_search.place(x=210, y=19)

    button_search = Button(GUI_read_mail, text="Search", width=10, command=event_search)
    button_search.place(x=585, y=15)

    listbox_labels_gmail = Listbox(
        GUI_read_mail, selectborderwidth=4, font=("Times New Roman", 12), width=20
    )
    listbox_labels_gmail.place(x=10, y=55)

    # interate mail_labels loop and insert it to listbox_labels_gmail
    lb_index = 0
    for lb in mail_labels:
        listbox_labels_gmail.insert(lb_index, f"{lb}")
        lb_index += 1

    listbox_labels_gmail.bind("<Double-Button-1>", extract_subjects_by_label_func)

    # info label Listbox
    # label_subject_mails = Label(GUI_read_mail, text="Mails")
    # label_subject_mails.place(x=210, y=10)

    # Listbox subject
    listbox_subject_mails = Listbox(
        GUI_read_mail, selectborderwidth=6, font=("Times New Roman", 12), width=55
    )
    listbox_subject_mails.place(x=210, y=55)

    # Bind view mail function to mail subject
    listbox_subject_mails.bind("<Double-Button-1>", view_mail_func)

    button_create_label = Button(
        GUI_read_mail, text="New mailbox", command=create_mailbox
    )
    button_create_label.place(x=10, y=370)

    button_delete_label = Button(
        GUI_read_mail, text="Delete mailbox", command=delete_mailbox
    )
    button_delete_label.place(x=100, y=370)

    button_back = Button(
        GUI_read_mail, text="Back", command=event_pressed_back, width=10
    )
    button_back.place(x=585, y=370)

    button_delete = Button(
        GUI_read_mail, text="Delete", command=event_pressed_delete, width=10
    )
    button_delete.place(x=490, y=370)

    # GUI_read_mail.protocol("WM_DELETE_WINDOW", on_close)
    GUI_read_mail.mainloop()


# display_read_mail("nhanth240500@gmail.com", "@177687Nhan@")
display_read_mail("nguyen.dphux@gmail.com", "Ilovesex123*")

