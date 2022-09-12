import openpyxl

work = openpyxl.load_workbook('Data/Items/main.xlsx')
wb = work.active
print(type(wb['D5'].value))