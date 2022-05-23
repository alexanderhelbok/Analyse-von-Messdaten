import numpy as np


def chisq(obs, exp, error):
    return np.sum((obs - exp) ** 2 / (error ** 2))


def test1(x, a):
    return a


def test2(x, a, b):
    return a*x + b


def test3(x, a, b, c):
    return a*x**2 + b*x + c


def test4(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d


def test5(x, a, b, c, d, e):
    return a*x + b*x**3 + c*x**2 + d*x + e


def test6(x, a, b, c, d, e, f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f


def test7(x, a, b, c, d, e, f, g):
    return a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g

