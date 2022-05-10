import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.optimize import curve_fit
from matplotlib.patches import Ellipse


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
print(param_cov)
xsp, ysp = np.sum(xi*alpha)/np.sum(alpha), np.sum(y*alpha)/np.sum(alpha)
print(f'xsp = {xsp}, ysp = {ysp}')
param2, param_cov2 = curve_fit(test2, xi, y, sigma=alpha)
print('A\u0305 = {}, B\u0305 = {}'.format(param2[0], param2[1]))
print(param_cov)
print(param_cov2)

# plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
# plt.plot(xi, test1(xi, param[0], param[1]), '--', color='blue', label='Normal Fit')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# ======== 2 ===============
ai, bi = np.linspace(1.85, 2.05, 50), np.linspace(9, 13, 50)
fun_map = np.empty((ai.size, bi.size))
for i in range(ai.size):
    for j in range(bi.size):
        fun_map[i, j] = chisq(y, test1(xi, ai[i], bi[j]), alpha) - chisq(y, test1(xi, param[0], param[1]), alpha)


r = np.corrcoef(xi, y)[0, 1]
print(f"HalbA = {np.sqrt(1+r)}, HalbB = {np.sqrt(1-r)}, Skew = {np.sqrt((1+r)/(1-r))}")


z = pd.DataFrame(fun_map)
z.columns = np.round((bi - param[1]), 2)
z.index = np.round((param[0] - ai), 2)
ax = sns.heatmap(z, vmin=0, vmax=5)
ax.hlines([14, 24.5, 35], color='k', *ax.get_xlim())
ax.vlines([12, 22.5, 33], color='k', *ax.get_xlim())
plt.show()
print(z.loc[0.05])

# fig, ax = plt.subplots()
# ell = Ellipse(xy=(0, 0), width=np.sqrt(1+r), height=np.sqrt(1-r), angle=np.sqrt((1+r)/(1-r)))
# ax.add_patch(ell)
# ax.set_aspect('equal')
# ax.autoscale()
# plt.show()

# =========== 4 ============
alit, blit = 2, 10
print(chisq(y, test1(xi, param[0], param[1]), alpha), chisq(y, test1(xi, alit, blit), alpha))
dchi = chisq(y, test1(xi, alit, blit), alpha) - chisq(y, test1(xi, param[0], param[1]), alpha)
P = 1 - np.exp(-dchi/2)
print(dchi, P)

