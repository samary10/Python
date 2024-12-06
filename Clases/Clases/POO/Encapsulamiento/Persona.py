#Encapsulamiento permite proteger los metodos 
#public por defecto 
#protecter va subrallado antes de la _variable da accesos a clases y sub clases 
#pribado __Nombre de la bariable 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self._edad=edad # protegida
        self.__CUENTABANCARIA=123456 # privada al ser una constante no es necesario recibirla como atributo 


    def mostrarInformacion(self):
        return f"nombre: {self.nombre} Edad: {self._edad}"
    

    def __mostrarCuenta(self):
        return f"Cuenta Bancaria {self.__CUENTABANCARIA}"
    
    def mostrarInformacionCompleta(self):
        return self.__mostrarCuenta()
    
persona1 = Persona("Sandra Martines", 35 )
print(persona1.nombre, persona1._edad)
print (persona1.mostrarInformacion())
print(persona1.mostrarInformacionCompleta())
