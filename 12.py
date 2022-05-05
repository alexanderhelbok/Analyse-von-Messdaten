import numpy as np
import xlrd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def chisq(obs, exp, error):
    return np.sum((obs - exp) ** 2 / (error ** 2))


# ========= 1 =========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(10)

i = np.linspace(1, 30, 30)
temp1, temp2, temp3 = [], [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))
    temp3.append(sheet.cell_value(i, 3))

xi, y, alpha = np.array(temp1), np.array(temp2), np.array(temp3)
w = np.reciprocal(alpha)**2


def test1(x, a, b):
    return a * x + b


def test2(x, a, b):
    return a * (x - xsp) + b


param, param_cov = curve_fit(test1, xi, y)
print('a\u0305 = {}, b\u0305 = {}'.format(param[0], param[1]))
xsp, ysp = np.sum(xi*alpha)/np.sum(alpha), np.sum(y*alpha)/np.sum(alpha)
print(f'xsp = {xsp}, ysp = {ysp}')
param2, param_cov2 = curve_fit(test2, xi, y)
print('A\u0305 = {}, B\u0305 = {}'.format(param2[0], param2[1]))


plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.plot(xi, test1(xi, param[0], param[1]), '--', color='blue', label='Normal Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# ======== 2 ===============
