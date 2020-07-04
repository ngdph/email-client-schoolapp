import email
import imaplib
import quopri
import base64
import re
from email import header


SERVER = "imap.gmail.com"


def get_labels(username, password):

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username, password)

    TOTAL_LABELS = 0
    LABELS = []

    RAW_LABELS = mail.list()[1]
    TOTAL_LABELS = len(mail.list()[1])

    for i in range(0, TOTAL_LABELS):
        LABEL = re.findall('"([^"]*)"', bytes.decode(RAW_LABELS[i], "utf-8"))[-1]

        LABELS.append(LABEL)
    return LABELS


def get_emails_id(username, password, label, search_string="ALL"):

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username, password)

    mail.select(f'"{label}"')

    status, data = mail.search(None, search_string)

    mailbox = {"label": "", "mailbox": []}
    mailbox["label"] = label

    mail_ids = []

    for block in data:
        mail_ids = block.split()

    return mail_ids[-7:]


def get_emails(username, password, label, search_string="ALL"):

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username, password)

    mail.select(f'"{label}"')

    status, data = mail.search(None, search_string)

    mailbox = {"label": "", "mails": []}
    mailbox["label"] = label

    mail_ids = []

    for block in data:
        mail_ids = block.split()

    # mail_ids = [mail_ids[-2]]

    for i in mail_ids:
        status, data = mail.fetch(i, "(RFC822)")

        mail_ = dict({"header": {}, "payload": []})

        for responsed_part in data:
            if isinstance(responsed_part, tuple):

                message = email.message_from_bytes(responsed_part[1])

                for field in message.items():
                    mail_["header"][field[0]] = field[1]

                    if field[0] in ["Subject", "From", "To"]:
                        mail_["header"][field[0]] = (
                            header.decode_header(field[1])[0][0] if field[1] else b""
                        )

                content_ = dict({"header": {}, "payload": {}})

                if message.is_multipart():
                    for message_part in message.get_payload():
                        if isinstance(message_part.get_payload(), list):
                            for items in message_part.get_payload():
                                for field in items.items():
                                    content_["header"][field[0]] = field[1]

                                    if field[0] in ["Subject", "From", "To"]:
                                        mail_["header"][field[0]] = (
                                            header.decode_header(field[1])[0][0] if field[1] else b""
                                        )

                                content_["payload"] = items.get_payload(decode=True)

                                mail_["payload"].append(content_)
                                content_ = dict({"header": {}, "payload": {}})

                        else:
                            for field in message_part.items():
                                content_["header"][field[0]] = field[1]

                            content_["payload"] = message_part.get_payload(decode=True)

                            mail_["payload"].append(content_)
                            content_ = dict({"header": {}, "payload": {}})

                else:
                    for field in message.items():
                        content_["header"][field[0]] = field[1]

                        if field[0] in ["Subject", "From", "To"]:
                            mail_["header"][field[0]] = (
                                header.decode_header(field[1])[0][0] if field[1] else b""
                            )

                    content_["payload"] = message.get_payload(decode=True)

                    mail_["payload"].append(content_)
                    content_ = dict({"header": {}, "payload": {}})

            # print(mail_)

        mailbox["mails"].append(mail_)

    return mailbox


# print(get_labels("nhanth240500@gmail.com", "@177687Nhan@"))
# a = get_emails("nhanth240500@gmail.com", "@177687Nhan@", "[Gmail]/Starred")
# print(a)
