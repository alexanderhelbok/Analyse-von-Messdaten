import numpy as np
import xlrd
import matplotlib.pyplot as plt

# ========== 1 ============
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(4)

y, alpha = [], []
x = np.linspace(0, 2, 21)

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    y.append(sheet.cell_value(i, 1))
    alpha.append(sheet.cell_value(i, 2))

# print(x,y,alpha)


def f1(a):
    # print(-0.1868 + 0.7752*a)
    return -0.1868 + 0.7752*a


def f2(a):
    # print(-0.1868 + 0.7752*a)
    return -0.0515 + 0.2963*a + 0.2272*a**2


def f3(a):
    # print(-0.1868 + 0.7752*a)
    return 1.0065 - 1.0090*np.cos(a)


chi = [0, 0, 0]
for i in range(0, len(x)):
    chi[0] += ((y[i] - f1(x[i])) / alpha[i])**2
    chi[1] += ((y[i] - f2(x[i])) / alpha[i])**2
    chi[2] += ((y[i] - f3(x[i])) / alpha[i])**2
    # print(((y[i] - f1(x[i]))/alpha[i])**2)

plt.errorbar(x, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.plot(x, f1(x), label='f1(x)')
plt.plot(x, f2(x), label='f2(x)')
plt.plot(x, f3(x), label='f3(x)')
plt.legend()
plt.show()

print(chi)
# =========== 3 ===========

sheet = wb.sheet_by_index(5)

y, alpha = [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    y.append(sheet.cell_value(i, 1))
    alpha.append(sheet.cell_value(i, 2))
x = np.linspace(0, 20, 21)


def f4(a, b, c):
    # print(-0.1868 + 0.7752*a)
    return b*a + c


plt.errorbar(x, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.plot(x, f4(x, 1.014, 9.59), label='f4(x)')
plt.legend()
plt.show()

s = 0
new1, new2 = [], []
for j in np.linspace(8, 11, 25):
    for i in range(0, len(y)):
        s += ((y[i] - f4(x[i], 1.014, j))/alpha[i])**2
    new1.append(s)

s = 0
for j in np.linspace(0.9, 1.13, 25):
    for i in range(0, len(y)):
        s += ((y[i] - f4(x[i], j, 9.59))/alpha[i])**2
    new2.append(s)


# print(new1, new2)
fig, axs = plt.subplots(2)
axs[0].plot(np.linspace(0.9, 1.13, 25), new2, label='X(a,b\u0305)')
axs[1].plot(np.linspace(8, 11, 25), new1, label='X(a\u0305,b)')
axs[0].legend()
axs[1].legend()
plt.show()
