import xlwt

wb = xlwt.Workbook(encoding="utf-8")
ws = wb.add_sheet("sheet1")
# for i in range(0, 9):
#     for j in range(0, i+1):
#         ws.write(i, j, "%d * %d = %d"%(i+1, j+1, (i+1)*(j+1)))
ws.write(1, 1, "hello")

wb.save("testXlwt.xls")