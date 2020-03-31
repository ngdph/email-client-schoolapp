def Generate_Key(text, key):
    key = list(key)
    if (len(text) == len(key)):
        return
    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])
    return ("".join(key))


def Encrypt_By_Algorithm(text, key):
    result = list()
    for i in range(len(text)):
        temp = (ord(text[i]) + ord(key[i])) % 26
        temp += ord('A')
        result.append(chr(temp))
    return ("".join(result))


def Decrypt_By_Algorithm(text, key):
    result = list()
    for i in range(len(text)):
        temp = (ord(text[i]) - ord(key[i]) + 26) % 26
        temp += ord('A')
        result.append(chr(temp))
    return ("".join(result))


plaintext = input("Nhập plaintext (Viết in hoa): ").strip()
keyword = input("Nhập keyword (Viết in hoa): ").strip()
print("-" * 100)
key = Generate_Key(plaintext, keyword)
ciphertext = Encrypt_By_Algorithm(plaintext, key)
print("Ciphertext :", ciphertext)
print("Original Text :", Decrypt_By_Algorithm(ciphertext, key))
