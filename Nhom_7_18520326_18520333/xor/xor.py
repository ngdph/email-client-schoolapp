# command: py xor.py crypto01.jpg uithcm

import sys

fileIn = sys.argv[1]
keyString = sys.argv[2]
fileOut = 'solved.jpg'


key = [ord(char) for char in keyString]

with open(fileIn, 'rb') as file_in:
    file_out = open(fileOut, 'wb')
    index = 0

    for crypted_bytes in file_in:
        xor = []
        i = 0

        for byte in crypted_bytes:
            xor.append(byte ^ key[(index + i) % len(key)])
            i += 1

        iterated_bytes = file_out.write(bytes(xor))
        index += iterated_bytes

    file_out.close()
