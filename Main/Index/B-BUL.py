# Variables

from ast import While


diametro = 1/4 , 3/16, 1/2, 5/8, 7/8, 3/4, 1

largo = 1/4, 3/16, 1/2, 3/4, 1

terminacion = "negro", "zincado"

cantidad_requerida = input()

# El usuario debe ingresar los atributos del bulon
# para verificar si el mismo esta disponible

#Ingresa los datos y verifica que los mismos son correctos"

print("Buen día! Gracias por elegirnos")
print("Seleccione el bulon que desea comprar")

diametro_input = input("Introduzca el diametro requerido  ")

if diametro_input == diametro:
    print("Introduzca el largo requerido ")
else:
    print("Error")


#    while True:
#    try:
#        edad = int(input("Escribe tu edad: "))
#    except ValueError:
#        print("Debes escribir un número.")
#        continue

#    if edad < 0:
#        print("Debes escribir un número positivo.")
#        continue
#    else:
#       break