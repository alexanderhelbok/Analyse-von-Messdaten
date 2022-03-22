import xlrd
import matplotlib.pyplot as plt
from numpy import exp
import numpy as np


# ========== 1 ===========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(2)

Data1 = []
Data2 = []
Time = []

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 1))
    Time.append(i)
    Data1.append(sheet.cell_value(i, 1))
    Data2.append(sheet.cell_value(i, 2))

print(Data1)
print(Data2)

plt.hist(Data1, density=False, bins=100)  # density=False would make counts
# plt.bar(Time, Data2, color="green")
plt.ylabel('#')
plt.xlabel('Data')
# plt.savefig('Data1.png')
# plt.show()


# =========== 2 ===========
def poisson(mean, x):
    sum = exp(-mean)*mean**x/np.math.factorial(x)
    return sum


mean1 = 1.657
std1 = mean1**0.5
mean2 = 1.209
std2 = mean2**0.5

p1 = round(poisson(mean1, 0) * poisson(mean2, 0), 3)
p2 = round(poisson(mean1, 3) * poisson(mean2, 1), 3)
p3 = p4 = p5 = 0

for i in range(0, 10):
    p3 += poisson(mean1, i)*poisson(mean2, i)

for i in range(0, 10):
    for j in range(i+1, 10):
        p4 += poisson(mean1, j)*poisson(mean2, i)

for i in range(0, 10):
    for j in range(i+1, 10):
        p5 += poisson(mean1, i)*poisson(mean2, j)

print('P(0:0) = {}, P(3:1) = {}'.format(p1, p2))
print('P(Heim) = {}, P(Unentschieden) = {}, P(Aus) = {}'.format(round(p4, 3), round(p3, 3), round(p5, 3)))

# ========== 3 =============
mean = 2

N0 = poisson(mean, 0)*365
N7 = 0
for i in range(7, 20):
    N7 += poisson(mean, i)*365

print('N(0) = {}, N(7+) = {}'.format(round(N0, 0), round(N7, 0)))
