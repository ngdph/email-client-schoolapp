from Crypto import Random
from Crypto.Util import Padding

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES, AES, PKCS1_v1_5
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import rsa
import unidecode

from secretpy import Caesar, Vigenere
from secretpy import alphabets

# Khởi tạo đối tượng SHA256 và đối tượng RSAKey với tham số là private key của người gửi
# Gọi hàm update + đối số và message để hash message và khi đó đối tượng SHA256 trả về message đã hash
# Gọi hàm sign của RSAKey và truyền tham số là đoạn hash => trả về chữ ký
def sign_message(message, private_key):
    signer = pkcs1_15.new(private_key)
    hashed_m = SHA256.new()
    hashed_m.update(message)
    signature = signer.sign(hashed_m)
    return signature


def generate_rsa_keys():
    key_pair = RSA.generate(2048)

    return (key_pair, key_pair.publickey())


def length_handler(data="", length=0):
    if len(data) < length:
        return Padding.pad(data.encode(), length)

    if len(data) > length:
        return data[0:15].encode()

    return data.encode()


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


def DES_Encrypt(plaintext, key, iv):
    handled_key = length_handler(key, DES.block_size)
    handled_iv = length_handler(iv, DES.block_size)

    cipher = DES.new(handled_key, DES.MODE_CBC, handled_iv)
    ciphertext = base64.b64encode(
        cipher.encrypt(Padding.pad(plaintext.encode(), DES.block_size))
    )

    return ciphertext


def DES_Decrypt(cipher, key, iv):
    handled_key = length_handler(key, DES.block_size)
    handled_iv = length_handler(iv, DES.block_size)

    ciphertext = base64.b64decode(cipher)

    crypt = DES.new(handled_key, DES.MODE_CBC, handled_iv)
    plaintext = Padding.unpad(crypt.decrypt(ciphertext), DES.block_size)

    return plaintext


def AES_Encrypt(plaintext, key, iv):
    handled_key = length_handler(key, 16)
    handled_iv = length_handler(iv, 16)

    cipher = AES.new(handled_key, AES.MODE_CBC, handled_iv)
    ciphertext = base64.b64encode(cipher.encrypt(Padding.pad(plaintext.encode(), 16)))

    return ciphertext


def AES_Decrypt(cipher, key, iv):
    handled_key = length_handler(key, 16)
    handled_iv = length_handler(iv, 16)

    ciphertext = base64.b64decode(cipher)

    crypt = AES.new(handled_key, AES.MODE_CBC, handled_iv)
    plaintext = Padding.unpad(crypt.decrypt(ciphertext), AES.block_size)

    return plaintext


def Generate_Key(text, key):
    key = list(key)
    if len(text) == len(key):
        return
    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])
    return "".join(key)


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


def new_alph(ch):
    ch = ch.lower()
    alph = "abcdefghijklmnopqrstuvwxyz"
    new_alph = alph[alph.index(ch) :] + alph[: alph.index(ch)]
    return new_alph


def Vigenere_Encrypt(text, key):
    big_key = key * (len(text) // len(key)) + key[: len(text) % len(key)]
    res = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1:
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res


def Vigenere_Decrypt(text, key):
    big_key = key * (len(text) // len(key)) + key[: len(text) % len(key)]
    res = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1:
                res += alph[new.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += alph[new.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res


def XOR_Encrypt(data, key):
    encrypted_bytes = bytes()

    encrypted_bytes.join(
        [data[index] ^ key[index % len(data)] for index in range(0, len(data))]
    )

