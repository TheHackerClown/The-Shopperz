import openpyxl

work = openpyxl.load_workbook('Data/Items/main.xlsx')
wb = work.active
print(type(wb['A2'].value))