from Crypto.Cipher import AES


def padding(s):
    return s.encode("utf-8") + b"{" * (16 - len(s) % 16)


def Encrypt_AES(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=b"0123456789abcdef")
    return cipher.encrypt(padding(plaintext))
    # .encrypt(padding(plaintext))


def Decrypt_AES(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=b"0123456789abcdef")
    decrypted_msg = cipher.decrypt(ciphertext).decode("utf-8")
    length_padding = decrypted_msg.count("{")
    return decrypted_msg[: len(decrypted_msg) - length_padding]


# message = "Hello World"
# print(message)

# iv = b"0123456789abcdef"
# private_key = b"Thai Hoang Nhan!"

# ciphertext = Encrypt_AES(message, private_key)
# print("Ciphertext: ", ciphertext)

# plaintext = Decrypt_AES(ciphertext, private_key)
# print("Plaintext: ", plaintext)
