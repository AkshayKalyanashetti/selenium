import pandas as PD
file_path = "C:/Users/Akshay/Downloads/demo.xlsx"
xl = PD.read_excel(file_path, sheet_name="Sheet1")
#print(xl)
column = xl[['User', 'Pass']]
#print(column)
row = xl[0:3]
s = xl.shape
print(s)
print(row.tail())
