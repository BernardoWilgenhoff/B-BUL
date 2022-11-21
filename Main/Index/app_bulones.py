# Variables
#Defino forma de importación del excel
import openpyxl
from openpyxl import workbook
from openpyxl import load_workbook



#Defino ubicación del archivo

# los diametros posibles de seleccionar son = 1, 2, 3, 4, 5
# los largos posibles de seleccionar son = 10, 20, 30, 40, 50
# las terminaciones posibles son = "negro", "zincado"

# El usuario debe ingresar los atributos del bulon
# para verificar si el mismo esta disponible

#Ingresa los datos y verifica que los mismos son correctos"

def verificacion_parametros():
    global diametro_input
    global largo_input
    global terminacion_input
    while True: 
        while True:
            try:
                diametro_input = int(input("Introduzca el diametro requerido: "))
            except ValueError:
                print("Debes escribir un numero")
                continue
            if diametro_input > 5 or diametro_input == 0:
                print("Ponga un numero válido 1, 2, 3, 4, 5")
            else:
                print("Pusiste numero válido")
                break
            continue

        while True:
            try:
                largo_input = int(input("Introduzca el largo requerido: "))
            except ValueError:
                print("Debes escribir un numero")
                continue
            if largo_input > 50:
                print("Ponga un numero válido 10, 20, 30, 40, 50")
            else:
                print("Pusiste numero válido")
                break
                continue

        while True:
            terminacion_input = (input("Introduzca la terminación requerida: "))
            if terminacion_input != "negro" and terminacion_input != "zincado":
                print("Ponga una terminación valida negro o zincado")
            else:
                print("Pusiste terminación válida")
                break
            continue
        
        print("Usted selecciono un bulón:")
        print(("Diametro:  ") + str(diametro_input))
        print(("Largo:  ") + str(largo_input))
        print(("Terminación:") + terminacion_input)
        print("Si el bulón que selecciono es correcto presione 1")
        print("De no ser correcto presione 0")
        paso_1 = int(input("Desea continuar "))
        if paso_1 == 0:
            print("Vuelva a seleccionar el bulón")        
        else:
            cantidad_requerida()
            break
        continue

def cantidad_requerida():
    while True:
        global cantidad_requerida
        try:
            cantidad_requerida = int(input("Introduzca la cantidad requerida: "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        if cantidad_requerida > 0:
            continuar_comprando()
        else:
            print("Debe colocar un numero positivo")
            break
        continue

def continuar_comprando ():
    print("Desea continuar comprando:")
    print("1: Seguir comprando")
    print("2: Ir a pagar")
    continuar = int(input("¿Que desea hacer? "))
    if continuar == 1:
        genero_superdescriptor()
        agregar_al_carrito()
    if continuar == 2:
        genero_superdescriptor()
        verificar_stock()

def genero_superdescriptor():
        global superd
        if terminacion_input == "negro":
            superd_terminacion = 1 
        if terminacion_input == "zincado":
            superd_terminacion = 2
        superd = str(diametro_input)+str(largo_input)+str(superd_terminacion)
        print(superd)
        print(cantidad_requerida)

def agregar_al_carrito():
    filesheet = ("C:\Desarrollo\GIT\B-BUL\B-BUL\Main\Index\data_base.xlsx")
    wb = load_workbook(filesheet)
    hoja_carrito = wb.create_sheet("Carrito")
    hoja_carrito["A1"] = "superdescriptor"
    hoja_carrito["A2"] = superd
    hoja_carrito["B2"] = "cantidad requerida"
    hoja_carrito["B2"] = cantidad_requerida
    wb.save(filesheet)

def verificar_stock():
    print("Ejecuta verificar stock")
    #cargamos el archivo
    filesheet = ("C:\Desarrollo\GIT\B-BUL\B-BUL\Main\Index\data_base.xlsx")
    wb = load_workbook(filesheet)
    sheet = wb['stock'] #cargamos la hoja

    #buscamos con el superdescriptor
    for cell in sheet["E"]:
        if cell.value == int(superd):
            print(sheet[f"D{cell.row}"].value)
            stock = int(sheet[f"D{cell.row}"].value)
            if stock >= cantidad_requerida:
                print("Gracias por su compra")
            else:
                print("Seleccione nueva cantidad:")
            continue



##############################################################################################################################
#                                                     ATENCION                                                                           #
#                                                                                                                            #
#                                       Empieza la ejecución del programa                                                    #
#                                                                                                                            #
#                                                                                                                            #
##############################################################################################################################

# Mensaje de bienvenida
print("Buen día! Gracias por elegirnos")
print("Seleccione el bulon que desea comprar")

# Permite al usuario instertar parámetros y verifica que sean correctos

verificacion_parametros()

