
from pylab import *
import numpy


import utils
def dis_sorted_log_of_visited_sku():
    l = []
    with open('../test_datas/most_visited_sku_1000', 'r') as f:
        for line in f:
            l.append(int(line.strip()))
    l.sort()
    l_log = [math.log(i,10) for i in l]
    for i in l_log:
        print "|",i,"|"

    X = np.linspace(0,1,len(l_log), endpoint=True)
    plot( l_log, X)
    show()

def dis_sorted_of_visited_sku_scatter():
    l = []
    with open('../test_datas/most_visited_sku_1000', 'r') as f:
        for line in f:
            l.append(int(line.strip()))
    l.sort()
    for i in l:
        print "|", i, "|"
    n = len(l)
    interval = float(1)/n
    X = []
    for i in range(0,n):
        X.append(i*interval)
    plt.scatter(X, l, alpha=0.5, cmap=plt.cm.hsv)



    z1 = np.polyfit(X,l,3)
    print z1
    p1 = np.poly1d(z1)
    print p1
    X = np.linspace(0, 1, len(l), endpoint=True)
    plot(X,p1(X))
    show()

def dis_sorted_of_visited_sku():
    l = []
    with open('../test_datas/most_visited_sku_1000', 'r') as f:
        for line in f:
            l.append(int(line.strip()))
    l.sort()
    for i in l:
        print "|",i,"|"
    X = np.linspace(0,1,len(l), endpoint=True)
    plot(X, l)

    show()
def dis_of_visited_sku():
    l = []
    with open("../test_datas/most_visited_sku_1000",'r') as f:
        for line in f:
            l.append(int(line.strip()))
    #l = [i/1000 for i in l]
    narray = numpy.array(l)
    sum = narray.sum()
    mean = float(sum) / narray.size

    l_new = [(i - mean) for i in l]

    d = utils.compute_frequency(l_new)
    plt.sca
    plt.scatter(d.keys(), d.values(), s=50,alpha=0.5, cmap=plt.cm.hsv)

    for k, v in d.iteritems():
        print k, ":", v
    #l_new.sort()
    #X = np.linspace(0, 1, len(l), endpoint=True)
    #plot(X, l_new)

    show()
if __name__ == "__main__":
    dis_sorted_of_visited_sku_scatter()
    #dis_sorted_log_of_visited_sku()
   #dis_sorted_of_visited_sku()
    #dis_of_visited_sku()
