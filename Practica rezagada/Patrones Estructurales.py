#Ejemplo segun el patron estructural Decorator
#Permite añadir funcionalidades a objetos de forma dinámica y flexible, sin modificar su estructura

class Bebida:
    def descripcion(self):
        return "Bebida básica"

    def costo(self):
        return 5

class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida

    def descripcion(self):
        return self.bebida.descripcion()

    def costo(self):
        return self.bebida.costo()

class Leche(DecoradorBebida):
    def descripcion(self):
        return self.bebida.descripcion() + ", con leche"

    def costo(self):
        return self.bebida.costo() + 2

class Chocolate(DecoradorBebida):
    def descripcion(self):
        return self.bebida.descripcion() + ", con chocolate"

    def costo(self):
        return self.bebida.costo() + 3

bebida = Bebida()
print(bebida.descripcion(), "costo:", bebida.costo())

bebida_leche = Leche(bebida)
print(bebida_leche.descripcion(), "costo:", bebida_leche.costo())

bebida_choco_leche = Chocolate(bebida_leche)
print(bebida_choco_leche.descripcion(), "costo:", bebida_choco_leche.costo())
