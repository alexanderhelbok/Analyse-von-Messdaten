import numpy as np
import xlrd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ========== 1 ============
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(6)

y, alpha = [], []
xi = np.linspace(1, 24, 24)

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    y.append(sheet.cell_value(i, 1))
    alpha.append(sheet.cell_value(i, 2))


def test(x, a, b):
    return a * x + b


plt.errorbar(xi, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.legend()
plt.show()


