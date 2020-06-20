# from OpenSSL import crypto
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding

# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.IO import PEM

import rsa

message = "this is a string"

p, q = rsa.generate_primes()
a, b = rsa.generate_primes()

public, private = rsa.generate_keys(p, q)
pub, priv = rsa.generate_keys(a, b)

digitalized_message = rsa.string_to_int(message)

first_phase = rsa.encrypt_rsa(digitalized_message, private)
second_phase = rsa.encrypt_rsa(first_phase, pub)

third_phase = rsa.decrypt_rsa(second_phase, priv)
forth_phase = rsa.decrypt_rsa(third_phase, public)

# print(signed, unsigned)
print(forth_phase, rsa.long_to_string(forth_phase))
# print(type(digitalized_message))
