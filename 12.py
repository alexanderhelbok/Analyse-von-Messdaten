import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
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


param, param_cov = curve_fit(test1, xi, y, sigma=alpha, absolute_sigma=True)

print('a\u0305 = {}, b\u0305 = {}'.format(param[0], param[1]))
print(np.corrcoef(xi, y))
xsp, ysp = np.sum(xi*alpha)/np.sum(alpha), np.sum(y*alpha)/np.sum(alpha)
print(f'xsp = {xsp}, ysp = {ysp}')
param2, param_cov2 = curve_fit(test2, xi, y, sigma=alpha)
print('A\u0305 = {}, B\u0305 = {}'.format(param2[0], param2[1]))
print(param_cov)
print(param_cov2)

# ======== 2 ===============
ai, bi = np.linspace(1.85, 2.05, 50), np.linspace(9, 13, 50)
fun_map = np.empty((ai.size, bi.size))
for i in range(ai.size):
    for j in range(bi.size):
        fun_map[i, j] = chisq(y, test1(xi, ai[i], bi[j]), alpha) - chisq(y, test1(xi, param[0], param[1]), alpha)


z = pd.DataFrame(fun_map)
z.columns = np.round((bi - param[1])/0.75, 0)
z.index = np.round((param[0] - ai)/0.05, 0)
ax = sns.heatmap(z, xticklabels=12, yticklabels=12, vmin=0, vmax=5)
plt.show()
