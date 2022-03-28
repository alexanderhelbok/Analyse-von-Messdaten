import xlrd
import matplotlib.pyplot as plt
import numpy as np
from statistics import fmean, stdev


def poisson(mean, x):
    sum = np.exp(-mean)*mean**x/np.math.factorial(x)
    return sum


# ========== 1 ===========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(2)

Data1, Data2, Time = [], [], []

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 1))
    Data1.append(sheet.cell_value(i, 1))
    Data2.append(sheet.cell_value(i, 2))

Data2.sort()
Data1.sort()
mean1 = fmean(Data1)
mean2 = fmean(Data2)

Poisson1, Poisson2 = [], []

for i in range(0, 60):
    Poisson1.append(poisson(mean1, i)*100)
    Poisson2.append(poisson(mean2, i)*100)
    Time.append(i)

# print(Data1)
# print(Data2)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(Data1, density=False, bins=60)  # density=False would make counts
ax1.plot(Time, Poisson1)
# plt.bar(Time, Data2, color="green")
# ax1.ylabel('#')
# ax1.xlabel('Data')
ax2.hist(Data2, density=False, bins=60)  # density=False would make counts
ax2.plot(Time, Poisson2)
# plt.savefig('Data1.png')
plt.show()


# =========== 2 ===========
mean1 = 1.657
std1 = mean1**0.5
mean2 = 1.209
std2 = mean2**0.5

p1 = round(poisson(mean1, 0) * poisson(mean2, 0), 3)
p2 = round(poisson(mean1, 3) * poisson(mean2, 1), 3)
p3, p4, p5 = 0, 0, 0

for i in range(0, 10):
    p3 += poisson(mean1, i)*poisson(mean2, i)

for i in range(0, 10):
    for j in range(i+1, 10):
        p4 += poisson(mean1, j)*poisson(mean2, i)

for i in range(0, 10):
    for j in range(i+1, 10):
        p5 += poisson(mean1, i)*poisson(mean2, j)

print('P(0:0) = {}, P(3:1) = {}'.format(p1, p2))
print('P(Heim) = {}, P(Unentschieden) = {}, P(Aus) = {}\n'.format(round(p4, 3), round(p3, 3), round(p5, 3)))

# ========== 3 =============
mean = 2

N0 = poisson(mean, 0)*365
N7 = 0
for i in range(7, 20):
    N7 += poisson(mean, i)*365

print('N(0) = {}, N(7+) = {}\n'.format(round(N0, 0), round(N7, 0)))

# =========== 4 ==========
mean1 = 2950
std1 = mean1**0.5
mean2 = 2660
std2 = mean2**0.5

Diff = mean1 - mean2
Err = (std1**2 + std2**2)**0.5

print('{} +- {}'.format(mean1, std1))
print('{} +- {}'.format(mean2, std2))
print('{} +- {}'.format(Diff, Err))
