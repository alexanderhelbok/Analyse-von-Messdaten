from scipy.stats import chi2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

colors_list = list(colors._colors_full_map.values())


def func(x, k, p):
    return chi2.sf(x, k) - p


def bisec(start, end, dof, p):
    while (end - start) > 0.001:
        mid = (start + end) / 2
        if func(mid, dof, p) < 0:
            end = mid
        else:
            start = mid
    return mid


p = [0.667, 0.95, 0.998]
for j in range(0, 3):
    temp1, temp2, temp3 = [], [], []
    for i in np.linspace(0.3, 50, 250):
        temp1.append(bisec(0, i+1, i, p[j])/i)
        temp2.append(bisec(i+1, 10*i+1, i, 1-p[j])/i)
        temp3.append(i)
    y1, y2, xi = np.array(temp1), np.array(temp2), np.array(temp3)
    plt.plot(xi, y1, label=f'{p[j]*100}%', color=colors_list[j+2])
    plt.plot(xi, y2, color=colors_list[j+2])

plt.hlines(y=1, xmin=0, xmax=50, linestyles='--')
plt.scatter(10, 1.2)
plt.xlim(0, 50)
plt.ylim(0, 3)
plt.legend()
plt.show()
