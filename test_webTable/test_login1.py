from test_webTable.test_login import test_logindemo
import pandas as PD
file_path = "C:/Users/Akshay/Downloads/practice.xlsx"
xl = PD.read_excel(file_path, sheet_name="Sheet1")
#rows = xl.get_rows(file_path, "Sheet1")
abc = xl.head(2)
print(abc)
#print(xl)

for i in range(0, xl):
    print(i)
    username = xl.get_data(file_path, "Sheet1", i, "UserName")
    password = xl.get_data(file_path, "Sheet1", i, "password")
    expected_result = xl.get_data(file_path, "Sheet1", i, "Expected_result")

    status = test_logindemo(username, password, expected_result)



