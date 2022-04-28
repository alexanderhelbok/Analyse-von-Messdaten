import numpy as np
import xlrd
import matplotlib.pyplot as plt


def chisq(obs, exp, error):
    return np.sum((obs - exp) ** 2 / (error ** 2))


# ========== 1 ============
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(4)

x = np.linspace(0, 2, 21)

temp1, temp2 = [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))

y, alpha = np.array(temp1), np.array(temp2)
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
chi[0] = chisq(y, f1(x), alpha)
chi[1] = chisq(y, f2(x), alpha)
chi[2] = chisq(y, f3(x), alpha)

print(chi)

plt.errorbar(x, y, yerr=alpha, fmt='.k', capsize=3, label='Data')
plt.plot(x, f1(x), label='f1(x)')
plt.plot(x, f2(x), label='f2(x)')
plt.plot(x, f3(x), label='f3(x)')
plt.legend()
plt.show()
# =========== 3 ===========

sheet = wb.sheet_by_index(5)

temp1, temp2 = [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))
x = np.linspace(0, 20, 21)
y, alpha = np.array(temp1), np.array(temp2)


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
