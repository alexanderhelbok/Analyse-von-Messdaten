import numpy as np
import xlrd
import matplotlib.pyplot as plt

# ========== 1 ============
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(6)

y, alpha = [], []
x = np.linspace(0, 24, 25)

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    y.append(sheet.cell_value(i, 1))
    alpha.append(sheet.cell_value(i, 2))


