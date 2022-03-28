import numpy as np
import xlrd
from statistics import fmean, stdev


def w(i):
    return 1/i**2

# =========== 1 ============
a, b = 9.8045, 9.8065
aerr, berr = 0.00012, 0.0009
wa, wb = 1/aerr**2, 1/berr**2

Y = (wa*a + wb*b)/(wa + wb)
y = (aerr*berr)/(aerr**2 + berr**2)**0.5
print('y\u0305 = {}, \u03B1 = \u00B1{}'.format(round(Y, 4), round(abs(y), 4)))
print("\n")
# ================ 2 =========

# ============== 3 ==========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(3)

Data, Err, rec = [], [], []

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 1))
    Data.append(sheet.cell_value(i, 1))
    Err.append(sheet.cell_value(i, 2))

for i in range(0, len(Data)):
    avg = (Data[i-1]*w(Err[i-1]) + Data[i]*w(Err[i]))/(w(Err[i-1]) + w(Err[i]))
    rec.append(1/Err[i]**2)

x = 1/(sum(rec))**0.5

Avg = fmean(Data)
sig = stdev(Data)/50**0.5
print('y\u0305 = {}, \u03B1 = \u00B1{}'.format(round(avg, 4), round(abs(x), 4)))
print('y\u0305 = {}, \u03B1 = \u00B1{}'.format(round(Avg, 4), round(abs(sig), 4)))
