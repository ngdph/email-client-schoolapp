from tkinter import *
from tkinter.ttk import Combobox
import re

import Caesar
import AES
import RSA


def decrypt_func(ciphertext):
    def caesar(ciphertext, key):
        result = Caesar.Caesar_Decrypt(ciphertext, key)
        return result

    def vigenere(cipher, key):
        return cipher

    def aes(ciphertext, key, iv):
        result = AES.AES_Decrypt(ciphertext, key, iv)
        return result

    def rsa(ciphertext, key):
        result = RSA.RSA_Decrypt(ciphertext, key)
        return result

    GUI_decrypted_box = Tk()
    GUI_decrypted_box.geometry("800x600")

    text_ciphertext = Text(GUI_decrypted_box, width=42, height=10)
    text_ciphertext.insert(INSERT, ciphertext, CHAR)
    text_ciphertext.place(x=10, y=30)

    text_plaintext = Text(GUI_decrypted_box, width=42, height=10)
    text_plaintext.insert(INSERT, ciphertext, CHAR)
    text_plaintext.place(x=320, y=30)
