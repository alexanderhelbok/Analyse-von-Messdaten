import numpy as np
# from uncertainties import *
import uncertainties as unc
import uncertainties.unumpy as unp
# from uncertainties.unumpy import *
import string

class ShorthandFormatter(string.Formatter):
    def format_field(self, value, format_spec):
        if isinstance(value, unc.UFloat):
            return value.format(format_spec+'S')  # Shorthand option added
            # Special formatting for other types can be added here (floats, etc.)
        else:
            # Usual formatting:
            return super(ShorthandFormatter, self).format_field(
                value, format_spec)


frmtr = ShorthandFormatter()
x = unc.ufloat(9.274, 0.005)
print(frmtr.format("Result = {0:.1uL}", x))  # 1-digit uncertainty

# ========= 1 =========
a = unc.ufloat(9.274, 0.005)
f1 = (a - 1) / (a + 1)
f2 = a**2/(a - 2)
f3 = unp.arcsin(1/a)
f4 = unp.log(1/a**0.5)
f5 = unp.exp(a**2)
print(f"y = {f1}", f"y = {f2}", f"y = {f3}", f"y = {f4}", f"y = {f5}", sep="\n")
print("\n")

# ========= 2 =========
a = unc.ufloat(12.3, 0.4)
b = unc.ufloat(5.6, 0.2)
c = unc.ufloat(89.0, 2.5)

f1 = (a-b)/(a+b)
f2 = a*b/c
f3 = a**2*b*c**3
f4 = unp.log(a*b**2*c)
f5 = unp.exp(a*b/c)

print(f"y = {f1}", f"y = {f2}", f"y = {f3}", f"y = {f4}", f"y = {f5}", sep="\n")
print("\n")

# ========= 3 =========
alpha = unc.ufloat(45, 0.1)*2*np.pi/360
beta = unc.ufloat(34.5, 0.2)*2*np.pi/360

f1 = unp.tan(alpha - beta)**2/unp.tan(alpha + beta)**2

print(f"R = {f1}")
print("\n")

# ========= 4 =========


# def d1(i, f, x):
#     h = 1.0*10**-6
#     result = (f(i, x) - f(i, x + h))/h
#     return result
#
#
# # =========== 1 =============
# a = 9.274
# err = 0.005
#
#
# def g1(i, x):
#     l = [(x-1)/(x+1), x**2/(x-2), np.arcsin(1/x), np.log2(1/a**0.5), np.exp(x**2)]
#     return l[i-1]
#
#
# for i in range(1, 6):
#     Yi = g1(i, a)
#     yi = d1(i, g1, a) * err
#     print('{}) y\u0305 = {}, \u03B1 = \u00B1{}'.format(i, round(Yi, 4), round(abs(yi), 4)))
#
# print("\n")
# # ============== 2 ===============
# a, b, c = 12.3, 5.6, 89.0
# aerr, berr, cerr = 0.4, 0.2, 2.5
#
#
# def g2(i, x, y, z):
#     l = [(x-y)/(x+y), x*y/z, x**2*y*z**3, np.log2(x*y**2*z), np.exp(x*y/z)]
#     return l[i-1]
#
#
# def d2(i, f, x):
#     h = 1.0*10**-6
#     if x == 'x':
#         result = (f(i, a, b, c) - f(i, a + h, b, c))/h
#     elif x == 'y':
#         result = (f(i, a, b, c) - f(i, a, b + h, c)) / h
#     elif x == 'z':
#         result = (f(i, a, b, c) - f(i, a, b, c + h)) / h
#     return result
#
#
# for i in range(1, 6):
#     Yi = g2(i, a, b, c)
#     yi = ((d2(i, g2, 'x') * aerr)**2 + (d2(i, g2, 'y') * berr)**2 + (d2(i, g2, 'z') * cerr)**2)**0.5
#     yirel = yi/Yi
#     print('{}) y\u0305 = {}, \u03B1 = \u00B1{}, \u03B1rel = \u00B1{}'.format(i, round(Yi, 4), round(abs(yi), 4), round(abs(yirel), 4)))
# print("\n")
# # ======================= 3 ========
# alpha, beta = 45.0*np. pi/180, 34.5*np. pi/180
# aerr, berr = 0.1*np. pi/180, 0.2*np. pi/180
#
#
# def g3(x, y):
#     return np.tan(x-y)**2/np.tan(x+y)**2
#
#
# def d3(f, x):
#     h = 1.0*10**-6
#     if x == 'x':
#         result = (f(alpha, beta) - f(alpha + h, beta))/h
#     elif x == 'y':
#         result = (f(alpha, beta) - f(alpha, beta + h)) / h
#     return result
#
#
# Yi = g3(alpha, beta)
# yi = ((d3(g3, 'x') * aerr)**2 + (d3(g3, 'y') * berr)**2)**0.5
# yirel = yi/Yi
# print('y\u0305 = {}, \u03B1 = \u00B1{}, \u03B1rel = \u00B1{}'.format(round(Yi, 4), round(abs(yi), 4), round(abs(yirel), 4)))
# print("\n")
# # ================ 4 =================
