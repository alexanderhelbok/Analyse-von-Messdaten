import xlrd
from numpy import pi, exp, sqrt, inf
from statistics import fmean, stdev
import mpmath as mp


# =========== 1 ===============
print("P_max = {}".format(round(1/(0.024*sqrt(2*pi)), 3)))
print()


# ======== 2 ==============
def dist(mean, std):
    f = lambda x: 1/(std*sqrt(2*pi))*mp.exp(-(x-mean)**2/(2*std**2))
    return f


def p(function, start, stop):
    result = mp.quad(function, [start, stop])
    return result


print("p1 = {}".format(round(p(dist(4.23, 0.78), 5.5, inf), 3)))
print("p2 = {}".format(round(p(dist(4.23, 0.78), -inf, 4.01), 3)))
print("p3 = {}".format(round(p(dist(4.23, 0.78), 3, 5), 3)))
print()

# ========== 3 ==============
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(1)

Data = []

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 1))
    Data.append(sheet.cell_value(i, 1))

Avg = fmean(Data)
Sigma = stdev(Data)
print("p = {}".format(round(mp.quad(lambda x : 1/(Sigma*sqrt(2*pi))*mp.exp(-(x-Avg)**2/(2*Sigma**2)), [9.806555, inf]), 5)))
