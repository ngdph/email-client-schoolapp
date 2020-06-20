from Crypto import Random
from Crypto.Util import Padding

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES, AES

import base64
import rsa

# class RSA:
#     def encrypt(self, plaintext, key):
#         ciphertext =


def RSA_Encrypt(plaintext, key):
    public_key = key.publickey().exportKey("PEM")

    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)

    encrypted_text = rsa_public_key.encrypt(plaintext)
    return encrypted_text


def RSA_Decrypt(ciphertext, key):
    private_key = key.export_key("PEM")
    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(ciphertext)
    return decrypted_text


def generate_rsa_keys():
    key_pair = RSA.generate(2048)

    return (key_pair.export_key(), key_pair.publickey().export_key())


def pad(plainbytes, block_size, style):
    return Padding.pad(plainbytes, block_size, style)


def unpad(cipherbytes, block_size, style):
    return Padding.unpad(cipherbytes, block_size, style)


def DES_Encrypt(plaintext, key, iv):
    cipher = DES.new(key.encode(), DES.MODE_CBC, iv.encode())
    ciphertext = cipher.encrypt(pad(plaintext.encode(), 16, "pkcs7"))

    result = base64.b64encode(ciphertext).decode()
    return result


def DES_Decrypt(ciphertext, key, iv):
    text = base64.b64decode(ciphertext)

    cipher = DES.new(key.encode(), DES.MODE_CBC, iv.encode())
    plaintext = cipher.decrypt(text)

    result = unpad(plaintext, 16, "pkcs7").decode()
    return result


def Caesar_Encrypt(plaintext, key):
    result = ""
    plaintext = plaintext.upper()
    for letter_index in range(len(plaintext)):
        char = plaintext[letter_index]
        m = ord(char)
        if m == 39:
            result = result + ","
        elif m == 46:
            result = result + "."
        elif m == 32:
            result = result + " "
        else:
            m = (m - 65 + key) % 26
            m = m + 65
            result = result + chr(m)
    return result


def Caesar_Decrypt(ciphertext, key):
    result = ""
    ciphertext = ciphertext.upper()
    for letter_index in range(len(ciphertext)):
        char = ciphertext[letter_index]
        m = ord(char)
        if m == 39:
            result = result + ","
        elif m == 46:
            result = result + "."
        elif m == 32:
            result = result + " "
        else:
            m = (m - 65 - key) % 26
            m = m + 65
            result = result + chr(m)
    return result


# def BruteForce(text, anphabet):
#     for key in range(len(anphabet)):
#         translated = ''
#         translated = Decrypt_By_Algorithm(text, 25 - key)
#         print('Key %s: %s' % (25 - key, translated))


# plaintext = input("Nhập plaintext: ")
# key = int(input("Nhập key: ").strip())
# print("-" * 100)
# ciphertext = Caesar_Encrypt(plaintext, key)
# print("Ciphertext: ", ciphertext)
# ori_text = Caesar_Decrypt(ciphertext, key)
# print("Original text: ", ori_text)
# print("-" * 100)
# print("Brute-force: ")
# BruteForce(ciphertext, anphabet)


def pad(plainbytes, block_size, style):
    return Padding.pad(plainbytes, block_size, style)


def unpad(cipherbytes, block_size, style):
    return Padding.unpad(cipherbytes, block_size, style)


def AES_Encrypt(plaintext, key, iv):
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    ciphertext = cipher.encrypt(pad(plaintext.encode(), 16, "pkcs7"))

    result = base64.b64encode(ciphertext).decode()
    return result


def AES_Decrypt(ciphertext, key, iv):
    text = base64.b64decode(ciphertext)

    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    plaintext = cipher.decrypt(text)

    result = unpad(plaintext, 16, "pkcs7").decode()
    return result


# mess = "abcdef"
# key = "0123456789abcdef"
# iv = "0123456789abcdef"

# print(AES_Encrypt(mess, key, iv))
# print(AES_Decrypt(AES_Encrypt(mess, key, iv), key, iv))


def Generate_Key(text, key):
    key = list(key)
    if len(text) == len(key):
        return
    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])
    return "".join(key)


def Vigenere_Encrypt(text, key):
    result = list()
    for i in range(len(text)):
        temp = (ord(text[i]) + ord(key[i])) % 26
        temp += ord("A")
        result.append(chr(temp))
    return "".join(result)


def Vigenere_Decrypt(text, key):
    result = list()
    for i in range(len(text)):
        temp = (ord(text[i]) - ord(key[i]) + 26) % 26
        temp += ord("A")
        result.append(chr(temp))
    return "".join(result)

