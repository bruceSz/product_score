import numpy
import matplotlib.pyplot as plt
from pylab import *
from scipy.optimize import curve_fit


def test_linear_fit():
    x = [i for i in range(1, 10)]
    y = x + numpy.random.randn(len(x))
    plt.scatter(x,y)
    pa = numpy.polyfit(x,y,1)
    y1 = numpy.poly1d(pa)
    axis = np.linspace(1, 10, 10, endpoint=True)
    plt.plot(axis,y1(axis))
    plt.show()


def test_cos_fit():
    x =  np.linspace(0,1,50)
    y =  numpy.cos(x)+0.1* numpy.random.rand(50)
    cof = numpy.polyfit(x,y,3)
    p = numpy.poly1d(cof)
    plt.plot(x,y,'o',x,p(x),lw=2)
    plt.show()

def exponent_fit():

    def func(x, a, b ,c):
        return a*numpy.exp(-b*x)+c

    xdata = numpy.linspace(0,4,50)
    y = func(xdata, 2.5, 1.3, 0.5)
    ydata = y+0.1*numpy.random.randn(len(xdata))
    popt , pcov = curve_fit(func, xdata, ydata)
    y2 = [func(i,popt[0],popt[1],popt[2]) for i in xdata]
    plt.plot(xdata,ydata,'o',xdata,y2,lw=1)
    plt.show()

if __name__ == "__main__":
    #test_linear_fit()
    #test_cos_fit()
    exponent_fit()
