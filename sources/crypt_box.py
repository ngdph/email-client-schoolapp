from tkinter import *
from tkinter.ttk import Combobox


import crypta


def decrypt_func(ciphertext, key):
    def caesar(ciphertext, key):
        result = crypta.Caesar_Decrypt(ciphertext, key) if key else ciphertext
        return result

    def vigenere(ciphertext, key):
        return ciphertext

    def aes(ciphertext, key, iv):
        result = crypta.AES_Decrypt(ciphertext, key, iv) if key else ciphertext
        return result

    def rsa(ciphertext, key):
        result = crypta.RSA_Decrypt(ciphertext, key) if key else ciphertext
        return result

    def event_pressed_send(event):
        pass

    def event_pressed_back(event):
        pass

    GUI_crypt_box = Tk()
    GUI_crypt_box.geometry("800x600")
    GUI_crypt_box.resizable(0, 0)

    label_sender_public_key = Label(GUI_crypt_box, text="Sender public key:")
    label_sender_public_key.place(x=20, y=300)

    label_user_private_key = Label(GUI_crypt_box, text="Your private key:")
    label_user_private_key.place(x=20, y=330)

    label_encrypted_key = Label(GUI_crypt_box, text="Encryption:")
    label_encrypted_key.place(x=20, y=370)

    label_encrypted_key = Label(GUI_crypt_box, text="Encrypted key:")
    label_encrypted_key.place(x=20, y=400)

    label_encrypted_iv = Label(GUI_crypt_box, text="Encrypted iv:")
    label_encrypted_iv.place(x=20, y=430)

    label_key = Label(GUI_crypt_box, text="Key:")
    label_key.place(x=420, y=400)

    label_iv = Label(GUI_crypt_box, text="IV:")
    label_iv.place(x=420, y=430)

    text_ciphertext = Text(GUI_crypt_box, wrap="word", width=45, height=15)
    text_ciphertext.insert(INSERT, ciphertext, CHAR)
    text_ciphertext.place(x=20, y=20)

    text_plaintext = Text(GUI_crypt_box, wrap="word", width=45, height=15)
    text_plaintext.insert(INSERT, caesar(ciphertext, key), CHAR)
    text_plaintext.place(x=410, y=20)

    sender_public_key = Entry(GUI_crypt_box, width=50)
    sender_public_key.configure(state=NORMAL)
    sender_public_key.place(x=150, y=300)

    user_private_key = Entry(GUI_crypt_box, width=50)
    user_private_key.configure(state=NORMAL)
    user_private_key.place(x=150, y=330)

    combobox_select_crypto = Combobox(
        GUI_crypt_box,
        values=["", "CAESAR", "VIGENERE", "AES", "DES"],
        width=17,
        state=NORMAL,
    )
    combobox_select_crypto.current(0)
    combobox_select_crypto.place(x=150, y=370)

    encrypted_key = Entry(GUI_crypt_box, width=40)
    encrypted_key.configure(state=NORMAL)
    encrypted_key.place(x=150, y=400)

    encrypted_iv = Entry(GUI_crypt_box, width=40)
    encrypted_iv.configure(state=NORMAL)
    encrypted_iv.place(x=150, y=430)

    key = Entry(GUI_crypt_box, width=40)
    key.configure(state=NORMAL)
    key.place(x=490, y=400)

    iv = Entry(GUI_crypt_box, width=40)
    iv.configure(state=NORMAL)
    iv.place(x=490, y=430)

    ### button để quay lại tab navigation
    button_back = Button(
        GUI_crypt_box, text="Back", command=event_pressed_back, width=10
    )
    button_back.place(x=20, y=520)

    # Button send
    button_send = Button(
        GUI_crypt_box, text="Decrypt", command=event_pressed_send, width=10
    )
    button_send.place(x=700, y=520)

    def event_selected_crypto(event):
        selected_type = combobox_select_crypto.get()
        if selected_type == "CAESAR" or selected_type == "VIGENERE":
            encrypted_iv.configure(state=DISABLED)
            iv.configure(state=DISABLED)
        else:
            encrypted_iv.configure(state=NORMAL)
            iv.configure(state=NORMAL)

    combobox_select_crypto.bind("<<ComboboxSelected>>", event_selected_crypto)

    GUI_crypt_box.mainloop()


decrypt_func("", "")

