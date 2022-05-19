import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.optimize import curve_fit
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms


def chisq(obs, exp, error):
    return np.sum((obs - exp) ** 2 / (error ** 2))


def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)


# ========= 1 =========
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(11)

i = np.linspace(1, 600, 600)
temp1, temp2 = [], []
for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    temp1.append(sheet.cell_value(i, 1))
    temp2.append(sheet.cell_value(i, 2))

xi, y = np.array(temp1), np.array(temp2)
xmean, ymean = np.mean(xi), np.mean(y)
cov = np.cov(xi, y)
xsig, ysig = np.sqrt(cov[0, 0]), np.sqrt(cov[1, 1])
r = cov[1, 0]/np.sqrt(cov[1, 1]*cov[0, 0])

print(f'x\u0305 = {xmean}, y\u0305 = {ymean}')
print(cov)
print(f'x\u03C3 = {xsig}, y\u03C3 = {ysig}, r = {r}')


fig, ax = plt.subplots()
ax.scatter(xi, y)
confidence_ellipse(xi, y, ax, n_std=1, edgecolor='red', label=r'$1\,\sigma$')
confidence_ellipse(xi, y, ax, n_std=2, edgecolor='red', label=r'$2\,\sigma$')
confidence_ellipse(xi, y, ax, n_std=3, edgecolor='blue', linestyle="--", label=r'$3\,\sigma$')
plt.legend()
plt.show()

# ========== 2 ==============
sheet = wb.sheet_by_index(12)

i = np.linspace(1, 50, 50)
temp1, temp2 = [], []
for set in range(0, 4):
    for i in range(1, sheet.nrows):
        # print(sheet.cell_value(i, 0))
        temp1.append(sheet.cell_value(i, 2+set*3))
        temp2.append(sheet.cell_value(i, 3+set*3))
    xi, y = np.vstack(np.array(temp1)), np.array(temp2)

print(xi)
