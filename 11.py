import numpy as np
import xlrd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def chisq(obs, exp, error):
    return np.sum((obs - exp) ** 2 / (error ** 2))


# ========== 1 ============
# infile = "datensaetze.xlsx"
#
# wb = xlrd.open_workbook(infile)
# sheet = wb.sheet_by_index(9)
#
# xi = np.linspace(1, 20, 20)
# temp1, temp2 = [], []
# for i in range(1, sheet.nrows):
#     # print(sheet.cell_value(i, 0))
#     temp1.append(sheet.cell_value(i, 1))
#     temp2.append(sheet.cell_value(i, 2))
#
# y, alpha = np.array(temp1), np.array(temp2)

# ============ 2 ==============
a, b, c = 7.953, -8.597, 28.378
sol = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
print('c\u0305 = {}'.format(sol))
