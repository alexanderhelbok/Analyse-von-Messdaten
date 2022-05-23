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
chi, rchi = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]


param, param_cov = curve_fit(test2, xi, y)
chi[0] = chisq(y, test2(xi, param[0], param[1]), alpha)/(len(xi) - 2)

plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.plot(xi, test2(xi, param[0], param[1]), '--', color='blue', label='Normal Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

param, param_cov = curve_fit(test3, xi, y)
chi[1] = chisq(y, test3(xi, param[0], param[1], param[2]), alpha)/(len(xi) - 3)
param, param_cov = curve_fit(test4, xi, y)
chi[2] = chisq(y, test4(xi, param[0], param[1], param[2], param[3]), alpha)/(len(xi) - 4)
param, param_cov = curve_fit(test5, xi, y)
chi[3] = chisq(y, test5(xi, param[0], param[1], param[2], param[3], param[4]), alpha)/(len(xi) - 5)
param, param_cov = curve_fit(test6, xi, y)
chi[4] = chisq(y, test6(xi, param[0], param[1], param[2], param[3], param[4], param[5]), alpha)/(len(xi) - 6)
param, param_cov = curve_fit(test7, xi, y)
chi[5] = chisq(y, test7(xi, param[0], param[1], param[2], param[3], param[4], param[5], param[6]), alpha)/(len(xi) - 7)

for i in range(0, 5):
    rchi[i] = stats.distributions.chi2.sf(chi[i], len(xi) - i+2)

print(chi, rchi)


