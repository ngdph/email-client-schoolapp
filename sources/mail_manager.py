from tkinter import *
from tkinter import simpledialog, messagebox
from mail_receiver import *
from detail_viewer import read_mail_func
import threading
from imapclient import IMAPClient
import pyisemail
from imap_tools import MailBox
import moving_dialog

# from future.moves.tkinter import simpledialog

label_index = 0
section_index = 0


def display_read_mail(username, password):
    # instance of tk
    GUI_read_mail = Tk()
    GUI_read_mail.title("Manage mail")
    GUI_read_mail.geometry("700x480")
    GUI_read_mail.resizable(0, 0)

    mail_labels = get_labels(username, password)
    selected_mail_index = 0
    mails = []
    mail_ids = []
    mail_sections = []

    current_mail = {}

    # Get mail
    def fetch_subjects_func(index_of_label, index_of_section):
        nonlocal mails
        nonlocal mail_ids
        nonlocal mail_sections

        listbox_subject_mails.delete(0, END)
        mails.clear()
        mail_ids.clear()
        mail_sections.clear()

        temp_mails_ids = get_emails_id(username, password, mail_labels[index_of_label])

        temp_ids = [
            temp_mails_ids[x : x + 10] for x in range(0, len(temp_mails_ids), 10)
        ]

        temp_sections = [index for index in range(0, len(temp_ids))]

        mail_ids = temp_ids
        mail_sections = temp_sections

        temp_mails = get_email_headers(
            username,
            password,
            mail_labels[index_of_label],
            mail_ids[mail_sections[index_of_section]],
        )

        for index, mail in enumerate(temp_mails):
            mails.append(mail)

            mail_subject = ""
            if "Subject" in mail:

                subject = mail["Subject"]

                if isinstance(subject, str):
                    if subject:
                        mail_subject = subject

                    else:
                        mail_subject = "(No subject)"

                if isinstance(subject, bytes):
                    mail_subject = subject.decode()

                    if not mail_subject:
                        mail_subject = "(No subject)"

            else:
                mail_subject = "(No subject)"

            listbox_subject_mails.insert(index, mail_subject)

        label_sections.configure(
            text=f"{section_index + 1 if len(mail_sections) > 0 else 0 }/{len(mail_sections)}"
        )

    def create_mailbox():
        mailbox_name = simpledialog.askstring(
            "New mailbox", "Mailbox name:", parent=GUI_read_mail
        )

        if mailbox_name:
            imap_client = imaplib.IMAP4_SSL("imap.gmail.com")
            imap_client.login(username, password)
            imap_client.create(f'"{mailbox_name}"')

            listbox_labels_gmail.delete(0, END)
            mail_labels = get_labels(username, password)
            lb_index = 0
            for lb in mail_labels:
                listbox_labels_gmail.insert(lb_index, f"{lb}")
                lb_index += 1

    def refresh():
        nonlocal mail_labels

        listbox_labels_gmail.delete(0, END)

        mail_labels.clear()
        mail_labels = get_labels(username, password)

        for lb_index, lb in enumerate(mail_labels):
            listbox_labels_gmail.insert(lb_index, f"{lb}")

        fetch_subjects_func(label_index, section_index)

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

    def extract_subjects_by_label_func(event):
        global label_index
        listbox_subject_mails.delete(0, "end")
        label_index = listbox_labels_gmail.curselection()[0]
        fetch_subjects_func(listbox_labels_gmail.curselection()[0], 0)

    def event_pressed_previous():
        global section_index

        if section_index <= 0:
            section_index = 0

        elif section_index > 0:
            section_index -= 1

        fetch_subjects_func(label_index, section_index)

    def event_pressed_next():
        global section_index

        if section_index <= 0:
            section_index = 1

        elif section_index > 0:
            section_index += 1

        fetch_subjects_func(label_index, section_index)

    def event_pressed_back():
        import navigation

        GUI_read_mail.destroy()
        navigation.display_navigation(username, password)

    def event_pressed_delete():
        import imaplib
        import ssl

        global label_index
        index = listbox_subject_mails.curselection()[0]
        mail_id = mail_ids[section_index][index]

        imap_client = imaplib.IMAP4_SSL("imap.gmail.com")
        imap_client.login(username, password)

        imap_client.select(f'"{mail_labels[label_index]}"')
        imap_client.uid("STORE", mail_id, "+X-GM-LABELS", "\\Trash")
        imap_client.expunge()

        fetch_subjects_func(label_index, section_index)

    def event_pressed_copy():
        nonlocal mail_labels
        mail_id = mail_ids[section_index][listbox_subject_mails.curselection()[0]]
        status = moving_dialog.moving_dialog(
            username, password, mail_labels[label_index], mail_labels, mail_id
        )

        fetch_subjects_func(label_index, section_index)

    def view_mail_func(event):
        nonlocal current_mail

        current_mail.clear()

        print(mail_ids[section_index][listbox_subject_mails.curselection()[0]])

        current_mail = get_emails(
            username,
            password,
            mail_labels[label_index],
            [mail_ids[section_index][listbox_subject_mails.curselection()[0]]],
        )

        read_mail_func(username, password, current_mail["mails"][0])

    def event_search():
        global label_index

        if entry_search.get():
            if entry_search.get().strip():
                query = [word.strip() for word in entry_search.get().split(":") if word.strip()]

                if len(query) == 2:
                    if (
                        query[0] == "FROM" or query[0] == "TO" or query[0] == "SUBJECT"
                    ) and (
                        (pyisemail.is_email(query[1]) and query[0] != "SUBJECT")
                        or (query[1].strip() and query[0] == "SUBJECT")
                    ):

                        search_string = (
                            r'(X-GM-RAW "subject:\"' + query[1] + r'\"")'
                            if query[0] == "SUBJECT"
                            else "(" + query[0] + ' "' + query[1] + '")'
                        )

                        nonlocal mails
                        nonlocal mail_ids
                        nonlocal mail_sections

                        listbox_subject_mails.delete(0, END)
                        mails.clear()
                        mail_ids.clear()
                        mail_sections.clear()

                        temp_mails_ids = get_emails_id(
                            username, password, "[Gmail]/All Mail", search_string
                        )

                        temp_ids = [
                            temp_mails_ids[x : x + 10]
                            for x in range(0, len(temp_mails_ids), 10)
                        ]

                        temp_sections = [index for index in range(0, len(temp_ids))]

                        mail_ids = temp_ids
                        mail_sections = temp_sections

                        temp_mails = get_email_headers(
                            username,
                            password,
                            "[Gmail]/All Mail",
                            temp_mails_ids,
                            search_string,
                        )

                        for index, mail in enumerate(temp_mails):
                            mails.append(mail)

                            mail_subject = ""
                            if "Subject" in mail:

                                subject = mail["Subject"]

                                if isinstance(subject, str):
                                    if subject:
                                        mail_subject = subject

                                    else:
                                        mail_subject = "(No subject)"

                                if isinstance(subject, bytes):
                                    mail_subject = subject.decode()

                                    if not mail_subject:
                                        mail_subject = "(No subject)"

                            else:
                                mail_subject = "(No subject)"

                            listbox_subject_mails.insert(index, mail_subject)

                        label_sections.configure(
                            text=f"{section_index + 1 if len(mail_sections) > 0 else 0 }/{len(mail_sections)}"
                        )

        else:
            messagebox.showerror("Error", "Search input is invalid.")

    entry_search = Entry(GUI_read_mail, width=60)
    entry_search.place(x=210, y=19)

    button_search = Button(GUI_read_mail, text="Search", width=10, command=event_search)
    button_search.place(x=585, y=15)

    listbox_labels_gmail = Listbox(
        GUI_read_mail, selectborderwidth=4, font=("Times New Roman", 12), width=20
    )
    listbox_labels_gmail.place(x=10, y=55)

    lb_index = 0
    for lb in mail_labels:
        listbox_labels_gmail.insert(lb_index, f"{lb}")
        lb_index += 1

    listbox_labels_gmail.bind("<Double-Button-1>", extract_subjects_by_label_func)

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
    button_create_label.place(x=10, y=440)

    button_update_label = Button(GUI_read_mail, text="Refresh", command=refresh)
    button_update_label.place(x=205, y=440)

    button_delete_label = Button(
        GUI_read_mail, text="Delete mailbox", command=delete_mailbox
    )
    button_delete_label.place(x=100, y=440)

    button_move = Button(
        GUI_read_mail, text="Copy", command=event_pressed_copy, width=10
    )
    button_move.place(x=395, y=390)

    label_sections = Label(GUI_read_mail)
    label_sections.place(x=350, y=390)

    button_previous = Button(
        GUI_read_mail, text="Previous", command=event_pressed_previous, width=10
    )
    button_previous.place(x=490, y=390)

    button_next = Button(
        GUI_read_mail, text="Next", command=event_pressed_next, width=10
    )
    button_next.place(x=585, y=390)

    button_delete = Button(
        GUI_read_mail, text="Delete", command=event_pressed_delete, width=10
    )
    button_delete.place(x=490, y=440)

    button_back = Button(
        GUI_read_mail, text="Back", command=event_pressed_back, width=10
    )
    button_back.place(x=585, y=440)

    GUI_read_mail.mainloop()


# display_read_mail("nhanth240500@gmail.com", "@177687Nhan@")
display_read_mail("18520165@gm.uit.edu.vn", "1634608674")
# display_read_mail("18520326", ".*")

