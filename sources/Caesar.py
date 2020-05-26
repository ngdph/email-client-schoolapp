import base64


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
