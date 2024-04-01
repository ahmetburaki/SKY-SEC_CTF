from Crypto.Util.number import *
from secret import FLAG1, FLAG2
from os import urandom

FLAG1 = bytes_to_long(FLAG1)
FLAG2 = bytes_to_long(FLAG2)

x, y, k = [getPrime(1024) for i in range(3)]

A = x * y

z = getPrime(2048)

B = z ** 3

C = bytes_to_long(urandom(31))
D = 65537

c1 = pow(FLAG1, k, A)
c2 = pow(FLAG2, D, B)

print(f"A = {A}")
print(f"B = {B}")
print(f"x+y = {x+y}")
print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"(C * A) + (2 * k) = {(C * A) + (2 * k)}")