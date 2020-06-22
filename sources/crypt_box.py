from tkinter import *
from tkinter.ttk import Combobox
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import cryptor
import unidecode


def decrypt_func(mail_content="", pub_key=""):

    signature = None
    cipher_message = None
    public_key = None

    GUI_crypt_box = Tk()
    GUI_crypt_box.title("Cryptbox")
    GUI_crypt_box.geometry("800x600")
    GUI_crypt_box.resizable(0, 0)

    plain_message = ""

    if pub_key:
        try:
            signature = bytes.fromhex(mail_content[-512:])
            pub = RSA.import_key(bytes.fromhex(pub_key))
            public_key = pkcs1_15.new(pub)
            cipher_message = mail_content.replace(mail_content[-512:], "")

            hashed_m = SHA256.new()
            hashed_m.update(cipher_message.encode())

            public_key.verify(hashed_m, signature)

        except Exception as e:
            print("This message had been tampered", e)

    def event_pressed_decrypt():
        selection = combobox_select_crypto.get()

        if selection == "CAESAR":
            plain_message = cryptor.Caesar_Decrypt(cipher_message, int(key.get()))

        if selection == "VIGENERE":
            handled_key = unidecode.unidecode(str(key.get()).lower().replace(" ", ""))
            plain_message = cryptor.Vigenere_Decrypt(cipher_message, handled_key)

        if selection == "AES":
            plain_message = cryptor.AES_Decrypt(cipher_message, key.get(), iv.get())

        if selection == "DES":
            plain_message = cryptor.DES_Decrypt(cipher_message, key.get(), iv.get())

        text_plaintext.insert(
            INSERT,
            plain_message.decode()
            if isinstance(plain_message, bytes)
            else plain_message,
            CHAR,
        )

    def event_pressed_back(event):
        pass

    text_ciphertext = Text(GUI_crypt_box, wrap="word", width=45, height=15)
    text_ciphertext.insert(INSERT, cipher_message, CHAR)
    text_ciphertext.place(x=20, y=20)

    text_plaintext = Text(GUI_crypt_box, wrap="word", width=45, height=15)
    text_plaintext.place(x=410, y=20)

    label_encrypted_key = Label(GUI_crypt_box, text="Encryption:")
    label_encrypted_key.place(x=20, y=280)

    label_key = Label(GUI_crypt_box, text="Key:")
    label_key.place(x=20, y=310)

    label_iv = Label(GUI_crypt_box, text="IV:")
    label_iv.place(x=20, y=340)

    combobox_select_crypto = Combobox(
        GUI_crypt_box,
        values=["", "CAESAR", "VIGENERE", "AES", "DES"],
        width=17,
        state=NORMAL,
    )
    combobox_select_crypto.current(0)
    combobox_select_crypto.place(x=150, y=280)

    key = Entry(GUI_crypt_box, width=40)
    key.configure(state=NORMAL)
    key.place(x=150, y=310)

    iv = Entry(GUI_crypt_box, width=40)
    iv.configure(state=DISABLED)
    iv.place(x=150, y=340)

    ### button để quay lại tab navigation
    button_back = Button(
        GUI_crypt_box, text="Back", command=event_pressed_back, width=10
    )
    button_back.place(x=20, y=520)

    # Button send
    button_decrypt = Button(
        GUI_crypt_box, text="Decrypt", command=event_pressed_decrypt, width=10
    )
    button_decrypt.place(x=700, y=520)

    def event_selected_crypto(event):
        selected_type = combobox_select_crypto.get()
        if selected_type == "CAESAR" or selected_type == "VIGENERE":
            iv.configure(state=DISABLED)
            iv.configure(state=DISABLED)
        else:
            iv.configure(state=NORMAL)
            iv.configure(state=NORMAL)

    combobox_select_crypto.bind("<<ComboboxSelected>>", event_selected_crypto)

    # GUI_crypt_box.mainloop()


# decrypt_func("")

