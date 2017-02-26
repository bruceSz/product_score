
import generate_nd
import utils

from pylab import *
import matplotlib.pyplot as plt
import numpy
import random

# follow such rules:
#  most values are near mu.
# like sigmoid function
def plot_sorted_gauss():
    l = generate_nd.sorted_gauss_numbers(1,1,1000)
    X = np.linspace(15, 20, 1000, endpoint=True)
    plot(l, X)

    show()



def plot_gauss():
    l  = generate_nd.raw_gauss_numbers(0,1,1000,1)
    narray = numpy.array(l)
    sum = narray.sum()
    mean = float(sum)/narray.size
    l_new = [ (i - mean) for i in l]



    d = utils.compute_frequency(l_new)
    #x = np.linspace(-2, 2, len(d.keys()), endpoint=True)
    plt.scatter(d.keys(), d.values(), alpha=0.5, cmap = plt.cm.hsv)
    #plot(d.values())
    #print plot.__doc__
    print d
    show()


# gauss number list's  frequency also gauss
def plot_nd_gauss():
    l = generate_nd.raw_gauss_numbers(0,1,10000, 2)
    d = {}
    for i in l:
        if i in d:
            #print 'met repeated'
            d[i] += 1
        else:
            d[i] = 1

    l.sort()

    x = d.keys()
    x.sort()
    l = d.values()
    #for i in x:
    #    print i
    plot(x, l)
    show()

def plot_his():
    mu, sigma = 100, 15
    x = mu + sigma*np.random.randn(1000)
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
    print x
    plt.grid()
    show()

# pure randome like white noise
def plot_raw_gauss():
    l = generate_nd.raw_gauss_numbers(0,1,1000)
    x = np.linspace(-1,1,1000,endpoint=True)
    plot(x,l)
    show()




if __name__ == "__main__":
    #plot_sorted_gauss()
    #plot_raw_gauss()
    #plot_nd_gauss()
    #plot_his()
    plot_gauss()