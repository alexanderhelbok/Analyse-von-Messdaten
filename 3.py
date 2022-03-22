import xlrd
from statistics import fmean, stdev



#  ================== 1 ==================
infile = "datensaetze.xlsx"

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(0)

Data = []

for i in range(1, sheet.nrows):
    # print(sheet.cell_value(i, 1))
    Data.append(sheet.cell_value(i, 1))

Avg = fmean(Data)
Sigma = stdev(Data)
alpha = Sigma/(len(Data)**0.5)
print('x = {}, \u03C3 = {}, \u03B1 = {}'.format(round(Avg, 4), round(Sigma, 4), round(alpha, 4)))
print(u'x\u0305  = 2.5012(8)')
print()


# ============== 2 =============
N = 18**2
t = N/2
print("t = {} s".format(int(t)))
print()


# =============== 3 =====================
def f(p):
    for i in range(2, 10**100000):
        y = 1 / (2 * i - 2)**0.5
        if y <= p:
            return i
            break


print('N(0.2) = {}, N(0.1) = {}, N(0.05) = {}'.format(f(0.2), f(0.1), f(0.05)))

# outfile = openpyxl.load_workbook(infile[0])
# sheet = outfile.active
#
# for i in range(len(Event)):
#     if cols[i] <= 9:
#         sheet.cell(row=cols[i], column=52).value = Best[i]
#         sheet.cell(row=cols[i], column=53).value = Worst[i]
#         sheet.cell(row=cols[i], column=54).value = Avg[i]
#     elif cols[i - 1] <= 17:
#         sheet.cell(row=cols[i], column=14).value = Best[i]
#         sheet.cell(row=cols[i], column=15).value = Worst[i]
#         sheet.cell(row=cols[i], column=16).value = Avg[i]
#     elif cols[i - 1] <= 24:
#         sheet.cell(row=cols[i], column=5).value = Best[i]
#         sheet.cell(row=cols[i], column=6).value = Worst[i]
#
# outfile.save(infile[0])
# outfile.close()
