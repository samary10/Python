class Banco:
    TAZA_INTERES=0.03

    def __init__(self,nombre):
        self.nombre=nombre
    
    @classmethod
    def cambiarTasa(cls,nuevaTasa):
        cls.TAZA_INTERES =nuevaTasa
    @classmethod
    def convertirDolaresEuros(dolares):
        return dolares * 0.85
    
convercion1 =(200)
convercion2 =(500)
print()