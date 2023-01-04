##implementation of Diffie-Hellman key exchange
import time
import random

#pseudo primality test using Fermat's little theorem
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(1000):
        a = random.randint(2, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True

#generate a random prime number smaller than n

def generatePrime(n):
    while True:
        p = random.randint(2, n)
        if isPrime(p):
            return p
#fast exponentiation algorithm
def fast_exp(a, b, n):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return fast_exp((a*a) % n, b/2, n)
    else:
        return (a * fast_exp((a*a) % n, (b-1)/2, n)) % n



def main():
    # take a random prime number p
    t = time.time()
    num = generatePrime(10**200)
    print(num)
    #generate Alice and Bob's private keys
    a = random.randint(2, num-1)
    b = random.randint(2, num-1)
    print(a)
    print(b)
    #genrate a random number g
    g = random.randint(2, num-1)

    #calculate Alice and Bob's public keys
    A = fast_exp(g, a, num)
    B = fast_exp(g, b, num)
    print(f"Alice's public key: {A}")
    print(f"Bob's public key: {B}")
    #calculate Alice and Bob's shared secret keys
    sA = fast_exp(B, a, num)
    sB = fast_exp(A, b, num)
    print(f"Alice's shared secret key: {sA}")
    print(f"Bob's shared secret key: {sB}")

    print(time.time() - t)

if __name__ == '__main__':
    main()


def primitive_root(num):
    #generate a number g such that g is a primitive root of p
    g = random.randint(2, num-1)
    while True:
        if fast_exp(g, num-1, num) == 1:
            return g
        g = random.randint(2, num-1)


def order(g, num):
    #calculate the order of g modulo p
    for i in range(1, num):
        if fast_exp(g, i, num) == 1:
            return i