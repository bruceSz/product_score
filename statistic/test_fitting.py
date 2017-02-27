import numpy
import matplotlib.pyplot as plt
import pylab
def test_linear_fit():
    x = [i for i in range(1, 10)]
    y = x + numpy.random.randn(len(x))
    plt.scatter(x,y)
    pa = numpy.polyfit(x,y,1)
    y1 = numpy.poly1d(pa)
    axis = pylab.np.linspace(1, 10, 10, endpoint=True)
    plt.plot(axis,y1(axis))
    plt.show()

if __name__ == "__main__":
    test_linear_fit()
