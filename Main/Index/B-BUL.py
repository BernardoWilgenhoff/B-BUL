# Variables

from ast import While

from operator import concat

#Defino forma de importación del excel
import openpyxl
from openpyxl import workbook
#Defino ubicación del archivo

diametro = 1, 2, 3, 4, 5

largo = 10, 20, 30, 40, 50

terminacion = "negro", "zincado"

cantidad_requerida = input()

# El usuario debe ingresar los atributos del bulon
# para verificar si el mismo esta disponible

#Ingresa los datos y verifica que los mismos son correctos"

def verificacion_parametros():
    while True:
        try:
            diametro_input = int(input("Introduzca el diametro requerido: "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        if diametro_input != (1 or 2 or 3 or 4 or 5):
            print("Ponga un numero válido 1, 2, 3, 4 5")
        else:
            print("Pusiste numero válido")
            break
        continue

    while True:
        largo_input = int(input("Introduzca el largo requerido: "))
        if largo_input != 10:
            print("Pone 10")
        else:
            print("Pusiste 10")
            break
            continue

    while True:
        terminacion_input = (input("Introduzca la terminación requerida: "))
        if terminacion_input != "negro":
            print("Pone negro")
        else:
            print("Pusiste negro")
            break
        continue
     
    print("Usted selecciono un bulón:")
    print(("Diametro:  ") + str(diametro_input))
    print(("Largo:  ") + str(largo_input))
    print("Terminacion:" + str(terminacion_input))



def cantidad_requerida():
    while True:
        cantidad_requerida = int(input("Introduzca la cantidad requerida: "))
        if cantidad_requerida > 0:
            print("OK")
        else:
            print("Debe colocar un numero positivo")
            break
            continue

# Mensaje de bienvenida
print("Buen día! Gracias por elegirnos")
print("Seleccione el bulon que desea comprar")

# Permite al usuario instertar parámetros y verifica que sean correctos

verificacion_parametros()

    # Verifica que lo ingresado es lo deseado
print("Si el bulón que selecciono es correcto presione y")
print("De no ser correcto presione n")
paso_1 = input(("Desea continuar "))

if paso_1 == "n":
    verificacion_parametros
else:
    cantidad_requerida()
