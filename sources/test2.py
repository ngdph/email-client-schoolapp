# # # # # # from Crypto.Signature import pkcs1_15
# # # # # # from Crypto.PublicKey import RSA
# # # # # # from Crypto.Hash import SHA256

# # # # # # message = "Hello world"

# # # # # # hashed_m = SHA256.new()
# # # # # # hashed_m.update(message.encode())

# # # # # # priv_key = RSA.generate(2048)
# # # # # # p = RSA.generate(2048)
# # # # # # pub_key = priv_key.publickey()

# # # # # # signer = pkcs1_15.new(priv_key)

# # # # # # signature = signer.sign(hashed_m)

# # # # # # verifier = pkcs1_15.new(pub_key)
# # # # # # # print(hashed_m)
# # # # # # veri = verifier.verify(hashed_m, signature)
# # # # # # hexf = signature.hex()

# # # # # # pub = pub_key.export_key("DER")
# # # # # # ip = RSA.import_key(bytes.fromhex(pub.hex()))

# # # # # # print(ip)

# # # # # # # print(
# # # # # # #     pub,
# # # # # # #     RSA.import_key(bytes.fromhex(pub.hex())).export_key("DER"),
# # # # # # #     pub == RSA.import_key(bytes.fromhex(pub.hex())).export_key("DER"),
# # # # # # # )


# # # # # # # print(signature, veri)
# # # # # # # import datetime
# # # # # # # time = datetime.datetime.now().isoformat()
# # # # # # # print(type(time))

# # # # # # # m = b"zxcv"
# # # # # # # print(isinstance(m, bytes))

# # # # # # a = []

# # # # # # import cryptor

# # # # # # m = "Mg4ey+esMZrWulmqpGbEoyYZlXfhTgDQC0Qvv3ebIe9gd+KGB2Fwj9Q1cCqrXZ1F Mg4ey+esMZrWulmqpGbEoyYZlXfhTgDQC0Qvv3ebIe9gd+KGB2Fwj9Q1cCqrXZ1F3236be5ce0c5ec20c0f815af755da8f193bb5f34af8dd3e1e6ac96174101d6521f60093301e5ba1f934b80fa234252de7dbce2d3716cd7c4a04ae74693ba52b334cdc8561f26f494b184cb5c373d83625f8fb7e029cf2a9288320f1d236833bc71baaba8c8874f7face420cfa63cb856b00f9ca02c16c66ebd02709e0a22650044514bd0bae2cba8dd3cd59777228de00607d04b76ea446a7003a82df23e3b979bfa726a0d3674383da77dacfb2ec2a6d4c5ec33fb3512eebf2649144c40c9f13138ee7014a5a891cb4749226e5b94f677c7b6db1a4318fc532a7253d7cd185261b49159617872f25e9a91164c0830d6aaff3d1368bf14d52e9efc8e4a0480d4"

# # # # # # signature = bytes.fromhex(m[-512:])
# # # # # # cipher_message = m.replace(m[-512:], "")

# # # # # # # print(signature, cipher_message, m)


# # # # # import base64
# # # # # from Crypto.Cipher import AES
# # # # # from Crypto.Util import Padding


# # # # # cipher = AES.new(
# # # # #     Padding.pad(key.encode(), AES.block_size),
# # # # #     AES.MODE_CBC,
# # # # #     Padding.pad(iv.encode(), AES.block_size),
# # # # # )
# # # # # newcipher = AES.new(
# # # # #     Padding.pad(key.encode(), AES.block_size),
# # # # #     AES.MODE_CBC,
# # # # #     Padding.pad(iv.encode(), AES.block_size),
# # # # # )

# # # # # ciphertext = cipher.encrypt(Padding.pad(m.encode(), AES.block_size))

# # # # # b64 = base64.b64encode(ciphertext)
# # # # # d64 = base64.b64decode(b64.decode())
# # # # # import cryptor
# # # # # # print(d64)
# # # # # c = cryptor.AES_Encrypt(m, )
# # # # # plaintext = Padding.unpad(newcipher.decrypt(d64), AES.block_size)
# # # # # print(ciphertext)

# # # # # import cryptor

# # # # # m = "This is a test message from mah client."
# # # # # key = "123456"
# # # # # iv = "456789"

# # # # # ciphertext = cryptor.AES_Encrypt(m, key, iv)
# # # # # plaintext = cryptor.AES_Decrypt(ciphertext.decode(), key, iv)

# # # # # print(ciphertext, plaintext)

# # # # # from secretpy import Caesar, Vigenere
# # # # # from secretpy import alphabets
# # # # import unidecode

# # # # # alphabet = alphabets.ENGLISH
# # # # plaintext = unidecode.unidecode("thels jlKj lethế lkjslektj thế".lower())
# # # # key = unidecode.unidecode("ewrqưg").replace(" ", "")
# # # # # cipher = Vigenere()
# # # # # import unidecode`
# # # # print(plaintext, key)
# # # # # plaintext = unidecode.unidecode(plaintext.lower().replace(" ", ""))
# # # # # key = unidecode.unidecode(key.lower().replace(" ", ""))

# # # # # print(plaintext, key, type(plaintext), type(key))

# # # # # # print(plaintext)
# # # # # enc = cipher.encrypt(plaintext, key, alphabet)
# # # # # print(enc)
# # # # # dec = cipher.decrypt(enc, key, alphabet)
# # # # # print(dec)

# # # # # # print("=====================================")

# # # # # # print(plaintext)
# # # # # # use default english alphabet
# # # # # enc = cipher.encrypt(plaintext, key)
# # # # # print(enc)
# # # # # dec = cipher.decrypt(enc, key)
# # # # # print(dec)
# # # # import cryptor

# # # # dec = cryptor.Vigenere_Encrypt(plaintext, key)
# # # # enc = cryptor.Vigenere_Decrypt(dec, key)
# # # # print(dec, enc)

# # # # a = b"a"
# # # # b = b"b"

# # # # c =
# # # # print(c, type(c))

# # # t = "asdfkjas;lfkjwelkfjwefk"

# # # print

# # import mail_receiver

# # ids = mail_receiver.get_emails_id("nguyen.dphux@gmail.com", ".*", "[Gmail]/All Mail")
# # print(len(ids))

# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.

# query = [word for word in "from    :    nguyen@mfila     ".split(" ") if word.strip()]
# print(query)
