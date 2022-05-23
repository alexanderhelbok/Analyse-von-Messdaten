import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import uncertainties as unc
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit
from main import *
# ========= 1 =========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(17)

xi = np.linspace(-10, 10, 41)
temp1, temp2, temp3 = [], [], []
for i in range(1, sheet.nrows):
    print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))
    # temp3.append(sheet.cell_value(i, 3))

y, alpha = np.array(temp1), np.array(temp2)
chi = []


for i in range(2, 7):
    param, param_cov = curve_fit(test(grad=i), xi, y)
    chi[i-2] = chisq(y, test(xi, param[0], param[1]), alpha)
