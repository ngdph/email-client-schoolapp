from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Label
from Crypto.Hash import SHA256, SHA512
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.IO import PEM
import cryptor
import unidecode
import tkinter


def decrypt_func(mail_content, signature_hex="", pub_key_hex=""):

    cipher_message = mail_content.decode()
    hashed_message = ""
    signature = ""
    public_key = ""

    GUI_crypt_box = Tk()
    GUI_crypt_box.title("Crypt Box")
    GUI_crypt_box.geometry("800x600")
    GUI_crypt_box.resizable(0, 0)

    plain_message = ""

    if pub_key_hex and signature_hex:
        try:
            signature = bytes.fromhex(signature_hex)
            pub_key = RSA.importKey(
                PEM.encode(bytes.fromhex(pub_key_hex), "PUBLIC KEY")
            )
            public_key = pkcs1_15.new(pub_key)

            cipher_message = mail_content.decode()
            print(cipher_message)
            hashed_m = SHA256.new()
            hashed_m.update(cipher_message.encode())

            public_key.verify(hashed_m, signature)
            hashed_message = signature_hex

        except Exception as e:
            print(e)
            print("This message is invalid", e)
            # messagebox.showerror("The signature of this mail is invalid.",)

    if not mail_content:
        cipher_message = "Not supported yet"
        plain_message = ""

    def event_pressed_decrypt():
        plain_message = "Please choose decryption type"

        if text_plaintext.get("1.0", "end"):
            text_plaintext.delete("1.0", "end")

        selection = combobox_select_crypto.get()
        try:

            if selection == "CAESAR":
                plain_message = cryptor.Caesar_Decrypt(
                    cipher_message, int(entry_key.get())
                )

            if selection == "VIGENERE":
                handled_key = unidecode.unidecode(
                    str(entry_key.get()).lower().replace(" ", "")
                )
                plain_message = cryptor.Vigenere_Decrypt(cipher_message, handled_key)

            if selection == "AES":
                plain_message = cryptor.AES_Decrypt(
                    cipher_message, entry_key.get(), entry_iv.get()
                )

            if selection == "DES":
                plain_message = cryptor.DES_Decrypt(
                    cipher_message, entry_key.get(), entry_iv.get()
                )

            if not text_plaintext.compare("end-1c", "==", "1.0"):
                text_plaintext.delete("1.0", END)

            text_plaintext.insert(
                INSERT,
                plain_message.decode()
                if isinstance(plain_message, bytes)
                else plain_message,
                CHAR,
            )
        except Exception as e:
            text_plaintext.insert(
                INSERT, str(e) if selection else plain_message, CHAR,
            )

    text_ciphertext = Text(GUI_crypt_box, wrap="word", width=45, height=15)
    text_ciphertext.insert(INSERT, cipher_message)
    text_ciphertext.place(x=20, y=20)

    text_plaintext = Text(GUI_crypt_box, wrap="word", width=45, height=15)
    text_plaintext.place(x=410, y=20)

    label_encrypted_key = Label(GUI_crypt_box, text="Encryption:")
    label_encrypted_key.place(x=20, y=280)

    label_key = Label(GUI_crypt_box, text="Key:")
    label_key.place(x=20, y=310)

    label_iv = Label(GUI_crypt_box, text="IV:")
    label_iv.place(x=20, y=340)

    label_signature = Label(GUI_crypt_box, text="Signature")
    label_signature.place(x=20, y=370)

    label_verifying_status = Label(GUI_crypt_box, text="status")
    label_verifying_status.place(x=20, y=430)

    combobox_select_crypto = Combobox(
        GUI_crypt_box,
        values=["", "CAESAR", "VIGENERE", "AES", "DES"],
        width=17,
        state=NORMAL,
    )
    combobox_select_crypto.current(0)
    combobox_select_crypto.place(x=150, y=280)

    entry_key = Entry(GUI_crypt_box, width=40)
    entry_key.configure(state=DISABLED)
    entry_key.place(x=150, y=310)

    entry_iv = Entry(GUI_crypt_box, width=40)
    entry_iv.configure(state=DISABLED)
    entry_iv.place(x=150, y=340)

    entry_signature = Text(GUI_crypt_box, width=45, height=5)
    entry_signature.insert("1.0", signature_hex)
    entry_signature.configure(state=DISABLED)
    entry_signature.place(x=20, y=400)

    entry_hashed_message = Text(GUI_crypt_box, width=45, height=5)
    entry_hashed_message.insert("1.0", hashed_message)
    entry_hashed_message.configure(state=DISABLED)
    entry_hashed_message.place(x=410, y=400)

    # Button send
    button_decrypt = Button(
        GUI_crypt_box, text="Decrypt", command=event_pressed_decrypt, width=10
    )
    button_decrypt.place(x=350, y=520)

    def event_selected_crypto(event):
        selected_type = combobox_select_crypto.get()
        if selected_type == "CAESAR" or selected_type == "VIGENERE":
            entry_iv.configure(state=DISABLED)
            entry_iv.configure(state=DISABLED)
        else:
            entry_iv.configure(state=NORMAL)
            entry_iv.configure(state=NORMAL)

        if selected_type:
            entry_key.configure(state=NORMAL)
        else:
            entry_key.configure(state=DISABLED)
            entry_iv.configure(state=DISABLED)

    combobox_select_crypto.bind("<<ComboboxSelected>>", event_selected_crypto)

    # GUI_crypt_box.mainloop()


# decrypt_func("")

