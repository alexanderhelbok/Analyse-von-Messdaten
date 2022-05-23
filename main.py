import numpy as np


def chisq(obs, exp, error):
    return np.sum((obs - exp) ** 2 / (error ** 2))


def test(x, a, b, c, d, e, f, g, grad):
    if grad == 0:
        return a
    if grad == 1:
        return a*x + b
    if grad == 2:
        return a*x**2 + b*x + c
    if grad == 3:
        return a*x**3 + b*x**2 + c*x + d
    if grad == 4:
        return a*x**4 + b*x**3 + c*x**2 + d*x + e
    if grad == 5:
        return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    if grad == 6:
        return a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g

