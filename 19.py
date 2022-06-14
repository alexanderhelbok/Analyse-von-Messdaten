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
sheet = wb.sheet_by_index(22)

xi = np.linspace(1, 11, 11)
temp1, temp2, temp3 = [], [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))
    # temp3.append(sheet.cell_value(i, 3))

y, alpha = np.array(temp1), np.array(temp2)


def test1(x, a):
    return a


param, param_cov = curve_fit(test1, xi, y, sigma=alpha, absolute_sigma=True)
param1, param_cov1 = curve_fit(test1, xi, y, sigma=alpha, absolute_sigma=False)

print(param, param_cov)
print(param1, param_cov1)

plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.hlines(y=param, xmin=0, xmax=12, label='Mean')
plt.hlines(y=param + np.sqrt(param_cov), xmin=0, xmax=12, linestyle='--', label='Sigma unscaled')
plt.hlines(y=param - np.sqrt(param_cov), xmin=0, xmax=12, linestyle='--')
plt.xlim(0, 12)
plt.ylim(18, 28)
plt.legend()
plt.show()


plt.errorbar(xi, y, yerr=alpha*np.sqrt(chisq(y, param, alpha)), fmt='.k', capsize=3, label='Data scaled')
plt.hlines(y=param, xmin=0, xmax=12, label='Mean')
plt.hlines(y=param + np.sqrt(param_cov1), xmin=0, xmax=12, linestyle='--', label="sigma scaled")
plt.hlines(y=param - np.sqrt(param_cov1), xmin=0, xmax=12, linestyle='--')
plt.xlim(0, 12)
plt.ylim(18, 28)
plt.legend()
plt.show()

