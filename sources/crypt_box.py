from tkinter import *
from tkinter.ttk import Combobox

import Caesar
import AES
import RSA


def decrypt_func(ciphertext, key):
    def caesar(ciphertext, key):
        result = Caesar.Caesar_Decrypt(ciphertext, key) if key else ciphertext
        return result

    def vigenere(ciphertext, key):
        return ciphertext

    def aes(ciphertext, key, iv):
        result = AES.AES_Decrypt(ciphertext, key, iv) if key else ciphertext
        return result

    def rsa(ciphertext, key):
        result = RSA.RSA_Decrypt(ciphertext, key) if key else ciphertext
        return result

    GUI_crypt_box = Tk()
    GUI_crypt_box.geometry("800x600")

    text_ciphertext = Text(GUI_crypt_box, wrap="word", width=43, height=10)
    text_ciphertext.insert(INSERT, ciphertext, CHAR)
    text_ciphertext.place(x=20, y=20)

    text_plaintext = Text(GUI_crypt_box, wrap="word", width=43, height=10)
    text_plaintext.insert(INSERT, caesar(ciphertext, key), CHAR)
    text_plaintext.place(x=430, y=20)

    label_encrypted_key = Label(GUI_crypt_box, text="Encrypted key:")
    label_encrypted_key.place(x=10, y=280)

    encrypted_key = Entry(GUI_crypt_box)
    encrypted_key.configure(state=NORMAL)
    encrypted_key.place(x=10, y=300)

    combobox_select_crypto = Combobox(
        GUI_crypt_box,
        values=["None", "Caesar", "Vigenere", "AES", "DES"],
        width=17,
        state=NORMAL,
    )
    combobox_select_crypto.current(0)
    combobox_select_crypto.place(x=150, y=280)

    def event_selected_crypto(event):
        selected_type = combobox_select_crypto.get()
        if selected_type == "Caesar" or selected_type == "Vigenere":
            entry_key.configure(state=NORMAL)

    combobox_select_crypto.bind("<<ComboboxSelected>>", event_selected_crypto)

    entry_key = Entry(GUI_crypt_box, state=NORMAL)
    entry_key.place(x=280, y=280)
