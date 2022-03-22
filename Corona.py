import xlrd
import re
import numpy as np
import matplotlib.pyplot as plt
# matplotlib inline


infile = "moscowcorona.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(0)

Data = []

for i in range(1, sheet.nrows):
    print(sheet.cell_value(i, 1))
    Data.append(float(re.sub("^[0-9]", "", str(sheet.cell_value(i, 1)))))

Data.sort()
print(Data)

np.random.seed(42)
x = np.random.normal(size=1000)

plt.hist(Data, density=False, bins=10)  # density=False would make counts
plt.ylabel('#')
plt.xlabel('Data')
plt.savefig('x_vs_t_A11a.png')
