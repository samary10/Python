class Empleado:
    def __init__(self, nombre, salario):
        self._nombre=nombre
        self._salario=salario

    def mostrarInformacion(self):
        return f"Nombre: {self._nombre} Salario: {self._salario}"

    def obtenetSalario(self):
        return self._salario

    def establecerSalario(self, nuevoSalario):
        # se toma como salario siempre y cuando sea mayor al minimo 
        if nuevoSalario < 1300000:
            return f"El salario es menor al minimo vigente"
        self._salario=nuevoSalario
        return f"El nuevo salario es {self._salario}"
    
    def asignacionesSalariales(self):
        pass

empleado1 = Empleado("Andres perez" , 1300000)
print(empleado1.mostrarInformacion)
print(empleado1.obtenetSalario)
print(empleado1.establecerSalario(1230000))
print(empleado1.establecerSalario(2000000))

