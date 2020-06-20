from Crypto import Random, IO
from Crypto.Util import Padding
from Crypto.IO import PEM
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES, AES, PKCS1_v1_5
import rsa
import base64

keychain = "alahuakbar"

# key = RSA.generate(1024)

# priv_key = key.export_key()
# iprt_priv = RSA.import_key(priv_key)

# priv = PKCS1_OAEP.new(iprt_priv)


# print(priv)
pub = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAki2YsWhfxGft4DNJ4eDv
ePzq1icCdTb7sSGTxOFQEmy/7wcSl5mwHNK4fk4HrzRSfwz6tYI3pimGn7ZfX3Qi
6lP2qoccn96UJvuvaOpJetdjMGYYuUEndtM9j7A6ozDKgB3ZvjWNRfDsuettztbd
w1kN1wGiximt1XFgmTozttwUG3zCaw8vLL8jxf0dKKpWcmsB4JrxZT2fo8vpH7hM
0V+e4A39OL7YcHoUv0X65EnFKhPDixEFHCP6lROmwKa1PyP4zCbge0rLxxy6oM7D
EyceX+60bqhOTY4Ap8YpNU2iWwSgbge0S9i7rnIAV3cxHszHs1hvZ/9czfIm66Fz
OQIDAQAB
-----END PUBLIC KEY-----"""


pub2 = """-----BEGIN RSA PRIVATE KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAki2YsWhfxGft4DNJ4eDv
ePzq1icCdTb7sSGTxOFQEmy/7wcSl5mwHNK4fk4HrzRSfwz6tYI3pimGn7ZfX3Qi
6lP2qoccn96UJvuvaOpJetdjMGYYuUEndtM9j7A6ozDKgB3ZvjWNRfDsuettztbd
w1kN1wGiximt1XFgmTozttwUG3zCaw8vLL8jxf0dKKpWcmsB4JrxZT2fo8vpH7hM
0V+e4A39OL7YcHoUv0X65EnFKhPDixEFHCP6lROmwKa1PyP4zCbge0rLxxy6oM7D
EyceX+60bqhOTY4Ap8YpNU2iWwSgbge0S9i7rnIAV3cxHszHs1hvZ/9czfIm66Fz
OQIDAQAB
-----END RSA PRIVATE KEY-----"""

priv = """-----BEGIN RSA PRIVATE KEY-----
MIIEoAIBAAKCAQEAki2YsWhfxGft4DNJ4eDvePzq1icCdTb7sSGTxOFQEmy/7wcS
l5mwHNK4fk4HrzRSfwz6tYI3pimGn7ZfX3Qi6lP2qoccn96UJvuvaOpJetdjMGYY
uUEndtM9j7A6ozDKgB3ZvjWNRfDsuettztbdw1kN1wGiximt1XFgmTozttwUG3zC
aw8vLL8jxf0dKKpWcmsB4JrxZT2fo8vpH7hM0V+e4A39OL7YcHoUv0X65EnFKhPD
ixEFHCP6lROmwKa1PyP4zCbge0rLxxy6oM7DEyceX+60bqhOTY4Ap8YpNU2iWwSg
bge0S9i7rnIAV3cxHszHs1hvZ/9czfIm66FzOQIDAQABAoIBAAz5t+n4hTa0kH6U
IujmW+9yCODrS8oukCMqIzko1GAcT+G2b6GuGl5GnKqWf9NfKjr9opQBy/GHklwD
Nt5M22wQOa8rqOBuhBldQjXmhRD+xT7Wszdfh5KiP97NMnlJo5IBhFJgY8rLbuH2
elPvyfXVBffZvPKI4NW3V48mZdCDgGu01yiMZitRKjJ5gpw+WDFiVdA9+Ix0uMLh
EaTwSHx0UXF+Y/+rY2DRhkhJbn/CVUFThSTyhMb7hAaOQG3gYOuaIS4IEz1aTkRG
W9U7owHCUkNFchxgCGP2/AaMjfu8HjoPTPN4jPIH63oUjMewoSFueFkVISUMUi/m
4vW7aWECgYEAtfwHiC/aQQfuzjxl9hYWsOtV/3r4OjLuUnFF1PaDyH2EYDBe4C5K
MgRvI/QJwIpgdRNZh7g8yDFC/nIGg7tkwC3GEwCrMaRjk7iGSHmHdzjCxNFlom3M
mms8NTHhfMwXqKEbXEs4/tbeu4vu8QzY9C6gTJxXwHWe6cx8l0q65mECgYEAzaF0
+vo2dJQUXIc+VWTyeLbBhWZX/GejhnHiLU9jniSoUVvPagyDLlY4UUThdrmFo23o
b5ZQQPdMNJaOHSVFAK5I6/y0KIqgrAPYPFzpiq/43/3I4P0KNJdM0/f+Z5VtUJpa
JC5b5owzgrp5j4DymDnlYz3iD8enYdmaWzIOC9kCgYB0erLrdQ1yEDzGXhw4zVyK
sqZhlnio745g0EWNEJe6zLPcyTkArkApEXN9hKZ1SVyBsvfcCY1F6Vni+GK5EEll
RCcCZKwuYvSlSTcRzk9pfLgVN52gwDx0Hez0c0/LC+qcsTmM8kyxuB/p1KAEQ1/d
srZBMtRryB0Fsi+QunE0IQKBgHdOHhkf40hwQgANV9Uj5Kq1HkLPxmzjlLUEjj3L
ufifPCk4I3dcGyBfVf2RAV9o9GiF9D4J8DZBRS2dzIaMgSSL+jMxQzXieKZU9LjR
D48v2i3biRlAtxMcVa8GS8y9ndcONw6W9yskXR6UIsNoBVjc/oI9/VM6e5sCLdSL
jirBAn8HOoZou35aSC08BLsnF57FYnnb3VWN2UMI+xSN7ew7bgr/Vo+U1iDI8YuD
ZldEzDqKbLB4WY/6PBFEt5J1AkH3jOOWeRF0L594ZxOTLZhXJSYr2i0WjuqmJZle
WvCqk+3ZyUzl2zWG2SAZmXvQegJvLoY7s/XAv6RRp1kLRjeP
-----END RSA PRIVATE KEY-----"""

pub_key = RSA.import_key(pub)
priv_key = RSA.import_key(priv)

pub_enc = PKCS1_v1_5.new(pub_key)
priv_enc = PKCS1_v1_5.new(priv_key)

# cipher = pub_enc.encrypt(keychain.encode())
# plain = priv_enc.decrypt(cipher)

signed = priv_enc.encrypt(keychain.encode())
unsigned = pub_enc.decrypt(signed, 'error')

print()

# print(cipher, plain)

# priv = PKCS1_OAEP.new(key)

# sign = key.encrypt(keychain, key.e)

# print(key.export_key())


# b = RSA.import_key(key.export_key())
# print(b.export_key())
