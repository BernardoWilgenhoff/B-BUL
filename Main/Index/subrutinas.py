from openpyxl import load_workbook
import app_bulones


def verificar_stock():
    #cargamos el archivo
    filesheet = ("C:\Desarrollo\GIT\B-BUL\B-BUL\Main\Index\data_base.xlsx")
    wb = load_workbook(filesheet)
    sheet = wb['stock'] #cargamos la hoja

    #pedimos un dato al usuario
    entrada = int(input("superdescriptor: "))

    for cell in sheet["E"]:
        if cell.value == entrada:
            print(sheet[f"D{cell.row}"].value)

