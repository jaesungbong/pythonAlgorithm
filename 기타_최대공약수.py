import math

a, b = 24, 12

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(a,b))

print(math.gcd(a,b))
