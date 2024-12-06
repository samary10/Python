#herencoa 
class Vehiculo:
    def __init__(self,tipo):
        self.tipo=tipo

    def descricion(self):
        return f"este vehiculo es de tipo {self.tipo}"

# moto es hijo de vehiculo y hereda el atributo marca
class Moto(Vehiculo):
    def __init__(self,tipo,marca):
        #con super se referencia el atributo eredado
        super().__init__(tipo)
        self.marca=marca

moto1 =Moto ("Motocicleta","Ducatti")
print(moto1.descricion())
    
