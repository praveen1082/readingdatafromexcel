import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell1 = sheet.cell(2, 1)

print(cell.value)
print(cell1.value)