from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from mail_receiver import get_labels, get_emails
from detail_viewer import read_mail_func


def display_read_mail(username, password):
    # instance of tk
    GUI_read_mail = Tk()
    GUI_read_mail.title("Đọc Mail")
    GUI_read_mail.geometry("700x400")
    GUI_read_mail.resizable(0, 0)

    labels = get_labels(username, password)
    label_index = 0
    selected_mail_index = 0
    mails = []

    # Get mail
    def fetch_subjects_func(index_of_label):
        # Xác định label
        # Lấy mail từ label
        # get_mails trả về dict chứa label và mails
        # Lấy value trong key mails
        temp_mails = get_emails(username, password, labels[index_of_label])["mails"]
        mail_index = 0

        # Xoá hết mail khi chọn label mới
        mails.clear()

        # Append mail subject to list box subject
        for mail in temp_mails:
            mails.append(mail)

            mail_subject = ""
            if mail["subject"]:
                mail_subject = mail["subject"]
            else:
                mail_subject = "No subject"

            listbox_subject_mails.insert(mail_index, mail_subject)
            mail_index += 1

    # Get mail subjects from label
    def extract_subjects_by_label_func(event):
        listbox_subject_mails.delete(0, "end")
        label_index = listbox_labels_gmail.curselection()[0]
        fetch_subjects_func(listbox_labels_gmail.curselection()[0])

    # Back button
    def event_pressed_back():
        import navigation

        GUI_read_mail.destroy()
        navigation.display_navigation(username, password)

    def view_mail_func(event):
        print(listbox_subject_mails.curselection()[0])
        read_mail_func(
            username, password, mails[listbox_subject_mails.curselection()[0]]
        )

    # Listbox Labels navigation
    label_gmail = Label(GUI_read_mail, text="Labels")
    label_gmail.place(x=10, y=10)

    listbox_labels_gmail = Listbox(
        GUI_read_mail, selectborderwidth=7, font=("Times New Roman", 12)
    )
    listbox_labels_gmail.place(x=10, y=30)

    # interate labels loop and insert it to listbox_labels_gmail
    lb_index = 0
    for lb in labels:
        print(lb, type(lb))
        listbox_labels_gmail.insert(lb_index, f"{lb}")
        lb_index += 1

    listbox_labels_gmail.bind("<Double-Button-1>", extract_subjects_by_label_func)

    # info label Listbox
    label_subject_mails = Label(GUI_read_mail, text="Mails")
    label_subject_mails.place(x=60, y=10)

    # Listbox subject
    listbox_subject_mails = Listbox(
        GUI_read_mail, selectborderwidth=6, font=("Times New Roman", 12), width=55
    )
    listbox_subject_mails.place(x=210, y=30)

    # Bind view mail function to mail subject
    listbox_subject_mails.bind("<Double-Button-1>", view_mail_func)

    # GUI_read_mail.mainloop()


# display_read_mail(username, password)
