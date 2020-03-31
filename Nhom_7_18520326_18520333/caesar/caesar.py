def Encrypt_By_Algorithm(text, key):
    result = ""
    for i in range(len(text)):
        letter = text[i]
        if (letter.isupper()):
            result += chr((ord(letter) + key - 65) % 26 + 65)
        else:
            result += chr((ord(letter) + key - 97) % 26 + 97)
    return result


def Decrypt_By_Algorithm(text, key):
    result = ""
    for i in range(len(text)):
        letter = text[i]
        if (letter.isupper()):
            result += chr((ord(letter) - key - 65) % 26 + 65)
        else:
            result += chr((ord(letter) - key - 97) % 26 + 97)
    return result


def BruteForce(text, anphabet):
    for key in range(len(anphabet)):
        translated = ''
        translated = Decrypt_By_Algorithm(text, 25 - key)
        print('Key %s: %s' % (25 - key, translated))


anphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext = input("Nhập plaintext: ")
key = int(input("Nhập key: ").strip())
print("-" * 100)
ciphertext = Encrypt_By_Algorithm(plaintext, key)
print("Ciphertext: ", ciphertext)
ori_text = Decrypt_By_Algorithm(ciphertext, key)
print("Original text: ", ori_text)
print("-" * 100)
print("Brute-force: ")
BruteForce(ciphertext, anphabet)
