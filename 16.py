import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import uncertainties as unc
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit
from scipy import stats
from main import *
# ========= 1 =========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(17)

xi = np.linspace(-10, 10, 41)
temp1, temp2, temp3 = [], [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))
    # temp3.append(sheet.cell_value(i, 3))

y, alpha = np.array(temp1), np.array(temp2)
chi, rchi, p = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]

param1, param_cov = curve_fit(test3, xi, y)
chi[0] = chisq(y, test3(xi, param1[0], param1[1], param1[2]), alpha)
param2, param_cov = curve_fit(test4, xi, y)
chi[1] = chisq(y, test4(xi, param2[0], param2[1], param2[2], param2[3]), alpha)
param3, param_cov = curve_fit(test5, xi, y)
chi[2] = chisq(y, test5(xi, param3[0], param3[1], param3[2], param3[3], param3[4]), alpha)
param4, param_cov = curve_fit(test6, xi, y)
chi[3] = chisq(y, test6(xi, param4[0], param4[1], param4[2], param4[3], param4[4], param4[5]), alpha)
param5, param_cov = curve_fit(test7, xi, y)
chi[4] = chisq(y, test7(xi, param5[0], param5[1], param5[2], param5[3], param5[4], param5[5], param5[6]), alpha)
param6, param_cov = curve_fit(test8, xi, y)
chi[5] = chisq(y, test8(xi, param6[0], param6[1], param6[2], param6[3], param6[4], param6[5], param6[6], param6[7]), alpha)

plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.plot(xi, test3(xi, param1[0], param1[1], param1[2]), '--', color='blue', label='Grad 2')
plt.plot(xi, test4(xi, param2[0], param2[1], param2[2], param2[3]), '--', color='gray', label='Grad 3')
plt.plot(xi, test5(xi, param3[0], param3[1], param3[2], param3[3], param3[4]), '--', color='green', label='Grad 4')
plt.plot(xi, test6(xi, param4[0], param4[1], param4[2], param4[3], param4[4], param4[5]), '--', color='magenta', label='Grad 5')
plt.plot(xi, test7(xi, param5[0], param5[1], param5[2], param5[3], param5[4], param5[5], param5[6]), '--', color='orange', label='Grad 6')
plt.plot(xi, test8(xi, param6[0], param6[1], param6[2], param6[3], param6[4], param6[5], param6[6], param6[7]), '--', color='black', label='Grad 7')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

plt.plot(chid(np.linspace(0, 10, 11), 5, 0.6))
plt.show()

for i in range(0, 6):
    rchi[i] = chi[i]/(len(xi) - i+2)
    p[i] = stats.distributions.chi2.sf(chi[i], len(xi) - i+2)
    print(f'\u03c7{i} = {rchi[i]}, p = {p[i]}', end='   ')
