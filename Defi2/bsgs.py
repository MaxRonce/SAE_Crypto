from DH_Key_exchange import *

from math import ceil, sqrt


def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None

def main_bsgs():
    # take a random prime number p
    num = generatePrime(10**6)
    print(f"p prime : {num}")
    a = random.randint(2, num - 1)
    print(f"number x: {a}")
    b = random.randint(2, num - 1)

    #solve for x in h = g^x mod p given a prime p
    print("solve for x in h = g^x mod p given a prime p")
    g = random.randint(2, num - 1)
    print(f"g: {g}")
    h = fast_exp(g, a, num)
    print(f"h: {h}")
    x = bsgs(g, h, num)
    print(f"x recovered with bsgs: {x}")
    #verify
    print(fast_exp(g, x, num) == h)



if __name__ == '__main__':
    main_bsgs()

