from Crypto.Cipher import AES
import string
import base64
from itertools import product

def decrypt(enc, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(base64.b64decode(enc))

ciphertext_b64 = b"PGmdN7ZVExS9GmisJcqtceupfRADGYWpy5ZVkBAI62I/YDnQk82OqjfKU2ntVHrD"
charlist = string.digits + string.ascii_letters

init = "DM"
iv = b'\x00' * 16

for c in product(charlist, repeat=4):
    key = init + ''.join(c)
    key = (key * 4).encode()
    try:
        plaintext = decrypt(ciphertext_b64, key, iv)
        if b"SKYSEC" in plaintext:
            print(plaintext)
            exit(0)
    except Exception as e:
        print(e)
        exit(1)
