from Crypto.Util.number import *
from hashlib import sha256
from secret import FLAG, p, b

F = GF(p)
E = EllipticCurve(F, [2, b])
G = E(51040877675655869648112904083888641850264277744136634711574761513961196864387, 34795863920624393818699532111363077979705508381454187790094917603186865372413)

ahmet_public_key = E(32639985269794158445863416533169376419205028688077377828259971565941927695679, 17911018872599344064269732011265352902866304744638706175366633247800987879746)
burak_public_key = E(23233193170339114409311794804286182477952045042048582069353495517218384068956, 33997750369905330916200197317015723658585732469881270308019974007882886286582)

def generatePrime(sz, d):
    while True:
        a = getRandomNBitInteger(sz)
        p = sum([a ** i for i in range(d)]) - a
        if isPrime(p):
            return p

def getModulus(p, q):
    return p * q

def encrypt(m, e, n):
    m = bytes_to_long(m)
    return pow(m, e, n)

def get_hash(x):
    hash = sha256()
    hash.update(long_to_bytes(x))
    return hash.digest()

hashes = [get_hash(p), get_hash(b)]

def gen_key(hash_list):
    return int(''.join(str(bytes_to_long(i + j)) for i in hash_list for j in hash_list))

r = generatePrime(1024, 3)
q = generatePrime(1024, 3)
e = 0x10001

n = getModulus(r, q)
c = encrypt(FLAG, e, n)

n += gen_key(hashes)

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")