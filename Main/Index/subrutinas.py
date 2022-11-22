
class Cuenta:
    contador = 1001

    def __init__(self, nombre):
        self.nombre = nombre
        self.numc = Cuenta.contador
        Cuenta.contador = Cuenta.contador + 1
