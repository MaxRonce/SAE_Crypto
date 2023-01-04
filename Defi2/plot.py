import numpy as np
import matplotlib.pyplot as plt
from DH_Key_exchange import *
from DLP import *
from bsgs import *

def Key_Exchange(a:int):
    # take a random prime number p
    num = generatePrime(10 ** a)

    # generate Alice and Bob's private keys
    a = random.randint(2, num - 1)
    b = random.randint(2, num - 1)

    # genrate a random number g
    g = random.randint(2, num - 1)

    # calculate Alice and Bob's public keys
    A = fast_exp(g, a, num)
    B = fast_exp(g, b, num)

    # calculate Alice and Bob's shared secret keys
    sA = fast_exp(B, a, num)
    sB = fast_exp(A, b, num)


def dh_plot():
    #plot the time to exchange keys with different values of a ( from 1 to 200 )
    x = np.arange(1, 200)
    y = np.zeros(199)
    for i in range(1, 200):
        print(i)
        start = time.time()
        Key_Exchange(i)
        end = time.time()
        y[i - 1] = end - start
    plt.plot(x, y)
    plt.xlabel("number of digits in p")
    plt.ylabel("time")
    plt.show()

def dlp(a:int):
    # same thing with bigger numbers
    num = DH_Key_exchange.generatePrime(2 ** a)

    # generate Alice and Bob's private keys
    a = random.randint(2, int(num - 1))
    b = random.randint(2, int(num - 1))


    g = random.randint(2, int(num / 2))

    # calculate Alice and Bob's public keys
    A = DH_Key_exchange.fast_exp(g, a, num)
    B = DH_Key_exchange.fast_exp(g, b, num)

    sA = DH_Key_exchange.fast_exp(B, a, num)
    sB = DH_Key_exchange.fast_exp(A, b, num)

    listA = []
    for i in range(1, num):
        temp = DH_Key_exchange.fast_exp(g, i, num)
        if temp == A:
            listA.append(i)

    listB = []
    for i in range(1, num):
        temp = DH_Key_exchange.fast_exp(g, i, num)
        if temp == B:
            listB.append(i)


    # calculate g^x mod p for each x in the list using lambda function
    resA = list(map(lambda x: DH_Key_exchange.fast_exp(B, x, num), listA))
    resB = list(map(lambda x: DH_Key_exchange.fast_exp(A, x, num), listB))

    intersection = list(set(resA) & set(resB))




def dlp_plot():
    #plot the time to exchange keys with different values of a ( from 6 to 24 )
    x = np.arange(6, 25)
    y = np.zeros(19)
    for i in range(6, 25):
        print(i)
        start = time.time()
        dlp(i)
        end = time.time()
        y[i - 6] = end - start
    plt.plot(x, y, label="brute force (optimized)")
    plt.xlabel("number of digits in p")
    plt.ylabel("time")



def bsgq_plot():
    #plot the time to solve a DLP problem with different values of a (from 3 to 48)
    x = np.arange(6, 47)
    y = np.zeros(41)
    for i in range(6, 47):
        print(i)
        start = time.time()
        main_bsgs(i)
        end = time.time()
        y[i - 6] = end - start
    plt.plot(x, y, label="bsgs")
    plt.xlabel("number of digits in p")
    plt.ylabel("time")







if __name__ == '__main__':
    #dh_plot()
    dlp_plot()
    bsgq_plot()
    #ajouter une légende pour chaque courbe





    plt.show()


