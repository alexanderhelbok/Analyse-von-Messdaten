import numpy as np
import xlrd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# from IPython.display import display, Math, Latex


def chisq(obs, exp, error):
    return np.sum((obs - exp) ** 2 / (error ** 2))


# ========== 1 ============
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(6)

xi = np.linspace(1, 24, 24)
temp1, temp2 = [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))

y, alpha = np.array(temp1), np.array(temp2)
w = np.reciprocal(alpha)**2


def test1(x, a, b):
    return a * x + b


param1, param_cov1 = curve_fit(test1, xi, y)
param2, param_cov2 = curve_fit(test1, xi, y, sigma=alpha)
chi1 = chisq(y, test1(xi, param1[0], param1[1]), alpha)
chi2 = chisq(y, test1(xi, param2[0], param2[1]), alpha)
print('a = {}, b = {}'.format(param1[0], param1[1]))
print('a = {}, b = {}\n'.format(param2[0], param2[1]))

plt.plot(xi, test1(xi, param1[0], param1[1]), '--', color ='blue', label=r'Normal Fit $\ \chi^2 \approx 110.0$')
plt.plot(xi, test1(xi, param2[0], param2[1]), '--', color ='orange', label=r"Weighted Fit $\ \chi^2 \approx 23.1$")
plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
# plt.ylim([-5, 25])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# ========== 2 ================
wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(7)

xi = np.linspace(1, 14, 14)
temp1, temp2 = [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))

y, alpha = np.array(temp1), np.array(temp2)
lit = 123.4567
avg = np.round(np.average(y, weights=alpha), 2)

print('\u03C7\u00b2 = {}, \u03C7\u00b2 = {}'.format(chisq(y, lit, alpha), chisq(y, avg, alpha)))
print('\u03BD = {}, \u03BD = {}'.format(len(y), len(y) - 2))
print('\u03C7\u00b2\u03BD = {}, \u03C7\u00b2\u03BD = {}\n'.format(chisq(y, lit, alpha)/len(y), chisq(y, avg, alpha)/(len(y) - 2)))

# ========== 3 ================
wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(8)

xi = np.linspace(10, 150, 15)
temp1, temp2 = [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))

y = np.array(temp1)

param, param_cov = curve_fit(test1, xi, y)
alph = (chisq(y, test1(xi, param[0], param[1]), 1)/(len(y) - 2))**0.5
print('\u03C7\u00b2 = {}'.format(chisq(y, test1(xi, param[0], param[1]), 1)))
print('\u03B1 = {}'.format(alph))

# plt.scatter(xi, y, s=25, color='black', label='Data')
plt.errorbar(xi, y, yerr=alph, fmt='.k', capsize=3, label='Data')
plt.plot(xi, test1(xi, param[0], param[1]), '--', color ='blue', label=r'Normal Fit $\ \chi^2 \approx 8171$')
plt.xlim([0, 160])
plt.ylim([0, 1000])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
