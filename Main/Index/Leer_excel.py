import pandas as pd
import openpyxl
from openpyxl import load_workbook


# datos = pd.read_csv("data_base.csv")
# print(datos[[""]])

#wb = "C:\Desarrollo\GIT\B-BUL\B-BUL\Main\Index\data_base.xlsx"

#datos = pd.read_excel("C:\Desarrollo\GIT\B-BUL\B-BUL\Main\Index\data_base.xlsx")

#print(datos)

datos = openpyxl.load_workbook("C:\Desarrollo\GIT\B-BUL\B-BUL\Main\Index\data_base.xlsx")

print(datos)



