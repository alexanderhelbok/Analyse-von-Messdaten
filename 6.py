import numpy as np


def d1(i, f, x):
    h = 1.0*10**-6
    result = (f(i, x) - f(i, x + h))/h
    return result


# =========== 1 =============
a = 9.274
err = 0.005


def g1(i, x):
    l = [(x-1)/(x+1), x**2/(x-2), np.arcsin(1/x), np.log2(1/a**0.5), np.exp(x**2)]
    return l[i-1]


for i in range(1, 6):
    Yi = g1(i, a)
    yi = d1(i, g1, a) * err
    print('{}) y\u0305 = {}, \u03B1 = \u00B1{}'.format(i, round(Yi, 4), round(abs(yi), 4)))

print("\n")
# ============== 2 ===============
a, b, c = 12.3, 5.6, 89.0
aerr, berr, cerr = 0.4, 0.2, 2.5


def g2(i, x, y, z):
    l = [(x-y)/(x+y), x*y/z, x**2*y*z**3, np.log2(x*y**2*z), np.exp(x*y/z)]
    return l[i-1]


def d2(i, f, x):
    h = 1.0*10**-6
    if x == 'x':
        result = (f(i, a, b, c) - f(i, a + h, b, c))/h
    elif x == 'y':
        result = (f(i, a, b, c) - f(i, a, b + h, c)) / h
    elif x == 'z':
        result = (f(i, a, b, c) - f(i, a, b, c + h)) / h
    return result


for i in range(1, 6):
    Yi = g2(i, a, b, c)
    yi = ((d2(i, g2, 'x') * aerr)**2 + (d2(i, g2, 'y') * berr)**2 + (d2(i, g2, 'z') * cerr)**2)**0.5
    yirel = yi/Yi
    print('{}) y\u0305 = {}, \u03B1 = \u00B1{}, \u03B1rel = \u00B1{}'.format(i, round(Yi, 4), round(abs(yi), 4), round(abs(yirel), 4)))
print("\n")
# ======================= 3 ========
alpha, beta = 45.0*np. pi/180, 34.5*np. pi/180
aerr, berr = 0.1*np. pi/180, 0.2*np. pi/180


def g3(x, y):
    return np.tan(x-y)**2/np.tan(x+y)**2


def d3(f, x):
    h = 1.0*10**-6
    if x == 'x':
        result = (f(alpha, beta) - f(alpha + h, beta))/h
    elif x == 'y':
        result = (f(alpha, beta) - f(alpha, beta + h)) / h
    return result


Yi = g3(alpha, beta)
yi = ((d3(g3, 'x') * aerr)**2 + (d3(g3, 'y') * berr)**2)**0.5
yirel = yi/Yi
print('y\u0305 = {}, \u03B1 = \u00B1{}, \u03B1rel = \u00B1{}'.format(round(Yi, 4), round(abs(yi), 4), round(abs(yirel), 4)))
print("\n")
# ================ 4 =================
