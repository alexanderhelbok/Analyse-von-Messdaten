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


param, param_cov = curve_fit(test1, xi, y, sigma=alpha, absolute_sigma=True)
print(param, param_cov)
a, b = unc.ufloat(param[0], np.sqrt(param_cov[0, 0])), unc.ufloat(param[1], np.sqrt(param_cov[1, 1]))
A = a**2/(2*b)
