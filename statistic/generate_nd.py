import math
import random

def print_e():
    print math.e

def generate_gauss_number(mu, sigma):
    while True:
        yield random.gauss(mu, sigma)

if __name__ == "__main__":
    gn = generate_gauss_number(1,1)
    r_list = []
    for i in range(0,100):
        r_list.append(gn.next())
    r_list.sort()
    for i in range(0,len(r_list)):
        print r_list[i]