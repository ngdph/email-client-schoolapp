from Crypto import Random, IO
from Crypto.Util import Padding
from Crypto.IO import PEM
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES, AES
import rsa
import base64

keychain = 'alahuakbar'

key = RSA.generate(1024)

priv_key = key.export_key()
iprt_priv = RSA.import_key(priv_key)

priv = PKCS1_OAEP.new(iprt_priv)



print(priv)

# priv = PKCS1_OAEP.new(key)

# sign = key.encrypt(keychain, key.e)

# print(key.export_key())


# b = RSA.import_key(key.export_key())
# print(b.export_key())
