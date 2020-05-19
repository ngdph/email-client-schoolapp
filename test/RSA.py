from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


def RSA_Encrypt(plaintext, key):
    public_key = key.publickey().exportKey("PEM")
    plaintext = str.encode(plaintext)

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


plaintext = "Tien ngu lon"
key = RSA.generate(2048)
ciphertext = rsa_encrypt(plaintext, key)
print("ciphertext ", ciphertext)
plain = rsa_decrypt(ciphertext, key)
print("plain ", plain)
