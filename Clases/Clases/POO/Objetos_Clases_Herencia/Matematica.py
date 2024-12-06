# Metodos estaticos , son comportamientos de una clase, no manejan instancias , no dependen de una clase  se identifican con el decorador @staticmethod
class Matematica:

    @staticmethod
    def suma(a,b):
        return a+b
    
    @staticmethod
    def resta(a,b):
        return a-b
    
print(Matematica.suma(10,10))
print(Matematica.resta(10,5))