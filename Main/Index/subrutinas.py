
class Cuenta:
    contador = 1001

    def __init__(self, nombre):
        self.nombre = nombre
        self.numc = Cuenta.contador
        Cuenta.contador = Cuenta.contador + 1


def continuar_comprando ():
    global continuar
    while True:
        print("Desea continuar comprando:")
        print("1: Seguir comprando")
        print("2: Ir a pagar")
        continuar = int(input("¿Que desea hacer? "))
        if continuar == 1:
            #genero_superdescriptor()
            #agregar_al_carrito()
            break
        else:
            #genero_superdescriptor()
            #verificar_stock()
            break
        continue

    cuenta_celdaA = 1
    cuenta_celdaB = 1
    #while True:
        #cuenta_celdaA += 1
        #cuenta_celdaB += 1
        #break
    #mem_n1 = str("A"+str(cuenta_celdaA))
    #mem_n2 = str("B"+str(cuenta_celdaB))
    #hoja_carrito2["A1"] = "superdescriptor"
    #hoja_carrito2[mem_n1] = superd
    #hoja_carrito2["B1"] = "cantidad"
    #hoja_carrito2[mem_n2] = cantidad_requerida
    #wb.save(filesheet)

def cantidad_requerida():
    global cantidad_requerida
    while True:
        try:
            cantidad_requerida = int(input("Introduzca la cantidad requerida: "))
        except ValueError:
            print("Debes escribir un numero")
        else:
            break
        continue

