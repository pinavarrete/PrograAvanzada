from math import exp
from numpy import random
import matplotlib.pyplot as plt
from functools import reduce


def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


def poisson(x, lambdaa=1):
    return (exp(-1*lambdaa) * (lambdaa)**x) / factorial(x)


if __name__ == '__main__':
    x = random.poisson(5, 10000)
    count, bins, ignored = plt.hist(x, 15, normed=True)
    plt.show()
