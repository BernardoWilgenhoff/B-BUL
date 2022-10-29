# Variables

from ast import While
from operator import concat

diametro = 1, 2, 3, 4, 5

largo = 10, 20, 30, 40, 50

terminacion = "negro", "zincado"

cantidad_requerida = input()

# El usuario debe ingresar los atributos del bulon
# para verificar si el mismo esta disponible

#Ingresa los datos y verifica que los mismos son correctos"

print("Buen día! Gracias por elegirnos")
print("Seleccione el bulon que desea comprar")

while True:
    diametro_input = int(input("Introduzca el diametro requerido: "))
    if diametro_input != 1:
        print("Pone 1")
    else:
        print("Pusiste 1")
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

