import numpy as np
import xlrd

# ========== 1 ============
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(4)

x, y, alpha = [], [], []

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 0))
    x.append(sheet.cell_value(i, 0))
    y.append(sheet.cell_value(i, 1))
    alpha.append(sheet.cell_value(i, 2))

a = -0.1868

for i in range(0, len(x)):
    chi = (y - )
#     rec.append(1/Err[i]**2)