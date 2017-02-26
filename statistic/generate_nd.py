import math
import random

def print_e():
    print math.e

def generate_gauss_number(mu, sigma):
    while True:
        yield random.gauss(mu, sigma)

def sorted_gauss_numbers(mu, sigma, size):
    gn = generate_gauss_number(mu, sigma)
    r_list = []
    for i in range(0,size):
        r_list.append(gn.next())

    r_list.sort()
    return r_list

def raw_gauss_numbers(mu, sigma, size, round_length):
    gn = generate_gauss_number(mu, sigma)
    l = []
    for i in range(0,size):
        l.append(round(gn.next(),round_length))
    return l


if __name__ == "__main__":
    gn = generate_gauss_number(1,1)
    r_list = []
    for i in range(0,100):
        r_list.append(gn.next())
    r_list.sort()
    for i in range(0,len(r_list)):
        print r_list[i]