import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import uncertainties as unc
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit

# ========= 1 =========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(13)

xi = np.linspace(1, 19, 19)
temp1, temp2, temp3 = [], [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))
    # temp3.append(sheet.cell_value(i, 3))

y, alpha = np.array(temp1), np.array(temp2)
yu = unumpy.uarray(y, alpha)
xu = unumpy.uarray(xi, 0)


def test1(x, a, b):
    return a * x + b


def test2(x, a, b):
    return -b**2/(2*a) * x + b


param, param_cov = curve_fit(test1, xi, y, sigma=alpha, absolute_sigma=True)
param1, param_cov1 = curve_fit(test2, xi, y, sigma=alpha, absolute_sigma=True)

# plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
# plt.plot(xi, test1(xi, param[0], param[1]), '--', color='blue', label=r'weighted Fit')
# plt.legend()
# plt.show()

a, b = unc.ufloat(param[0], np.sqrt(param_cov[0, 0])), unc.ufloat(param[1], np.sqrt(param_cov[1, 1]))
A = -b**2/(2*a)
print(f"A1 = {A}, A2 = {np.round(param1[0], 1)}({np.round(param_cov1[0, 0], 2)})")

# ========= 2 ================
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(14)

# xi = np.linspace(60, 140, 9)
temp1, temp2, temp3 = [], [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 0))
    temp2.append(sheet.cell_value(i, 1))
    temp3.append(sheet.cell_value(i, 2))

xi, y, alpha = np.array(temp1), np.array(temp2), np.array(temp3)
yu = unumpy.uarray(y, alpha)
xu = unumpy.uarray(xi, 0)
g = 9.805


def test3(x, a, b):
    return -g/(2*a**2*np.cos(b)**2)*x**2 + np.tan(b)*x


param, param_cov = curve_fit(test3, xi, y, sigma=alpha, absolute_sigma=True)

# plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
# plt.plot(np.linspace(0, 400, 400), test3(np.linspace(0, 400, 400), param[0], param[1]), '--', color='blue', label=r'weighted Fit')
# plt.xlim([0, 400])
# plt.ylim([0, 80])
# plt.legend()
# plt.show()

v, theta = unc.ufloat(param[0], np.sqrt(param_cov[0, 0])), unc.ufloat(param[1], np.sqrt(param_cov[1, 1]))
r = param_cov[0, 1]/(np.sqrt(param_cov[0, 0])*np.sqrt(param_cov[1, 1]))
R = v**2/g*unumpy.sin(2*theta)
h = v**2/(2*g)*unumpy.sin(theta)**2
print(f"v0 = {v}, \u0398 = {theta*180/np.pi}, r = {r}")
print(f"R = {R}, h = {h}")
