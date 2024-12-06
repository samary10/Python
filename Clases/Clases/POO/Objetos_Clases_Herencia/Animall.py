#metodos de clase 
class Animall:
    cantidadAnimales=0

    def __init__(self,name):
        self.name=name 
        Animall.cantidadAnimales += 1

    #decoradores tienen funciones como documentar, mutar comportamiento de un metodo 
    @classmethod
    # totalAnimales trae como argumento la clase cls
    def totalAnimales(cls):
        return f"Tengo{cls.cantidadAnimales} animales "

#instanciando objetos
animal1=Animall("Mia")
animal2=Animall("Luli")
animal3=Animall("Orion")
animal4=Animall("Loky")

print (Animall.totalAnimales)