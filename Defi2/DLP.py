#Brute force attck on a discrete log problem

import random
import DH_Key_exchange
import time

def main():
    #same thing with bigger numbers
    num = DH_Key_exchange.generatePrime(10**6)
    print(f"p prime : {num}")
    #generate Alice and Bob's private keys
    a = random.randint(2, int(num-1))
    b = random.randint(2, int(num-1))
    print("")
    print("-----private keys-----")
    print("")
    print(f"Alice's private key: {a}")
    print(f"Bob's private key: {b}")
    print("")
    #genrate a random number g
    print("-----public-----")
    print("")
    g = random.randint(2, int(num/2))
    print(f"g: {g}")

    #calculate Alice and Bob's public keys
    A = DH_Key_exchange.fast_exp(g, a, num)
    B = DH_Key_exchange.fast_exp(g, b, num)
    print(f"Alice's public key: {A}")
    print(f"Bob's public key: {B}")

    #calculate Alice and Bob's shared secret keys
    sA = DH_Key_exchange.fast_exp(B, a, num)
    sB = DH_Key_exchange.fast_exp(A, b, num)
    print("")
    print("-----private shared keys-----")
    print("")
    print(f"Alice's shared secret key : {sA}")
    print(f"Bob's shared secret key : {sB}")

    print("")
    print("-----attack-----")
    print("")


    start = time.time()
    listA = []
    listB = []
    for i in range(1, num):
        temp = DH_Key_exchange.fast_exp(g, i, num)
        if temp == A:
            listA.append(i)
        if temp == B:
            listB.append(i)

    print(f"list of possible Alice's private keys: {listA}")
    print(f"list of possible Bob's private keys: {listB}")

    #calculate Alice and Bob's shared secret keys
    sA = DH_Key_exchange.fast_exp(B, listA[0], num)
    sB = DH_Key_exchange.fast_exp(A, listB[0], num)

    print(f"Alice's shared secret key: {sA}")
    print(f"Bob's shared secret key: {sB}")

    end = time.time()
    print(f"Time: {end-start}")





if __name__ == '__main__':
    main()
