from Crypto.Cipher import DES
from Crypto.Util import Padding

import base64


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


# mess = "abcdef"
# key = "abcdefgh"
# iv = "abcdefgh"

# print(DES_Encrypt(mess, key, iv))
# print(DES_Decrypt(DES_Encrypt(mess, key, iv), key, iv))
