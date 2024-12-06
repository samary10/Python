class CuentaBancaria:
    def __init__(self, titular, saldo, clave):
        self.titular = titular
        self._saldo =saldo
        self.__clave=clave
        

    def deposito(self, cantidadDepositar):
        self._saldo += cantidadDepositar
        return f"Depoesito exitoso. Saldo actual {self._saldo}"

    def retirar(self, cantidadRetiro):
        if cantidadRetiro>self._saldo:
            return "Fondos insuficientes"
       
        self._saldo-=cantidadRetiro
        return f"retiro exitoso, su saldo actual es {self._saldo}"

    def modificarClave(self, nuevaClave):
        self.__clave=nuevaClave
        return f"la clave se cambio correctamente, la clave es: {self.__clave}"
    
cuentaBancaria1=CuentaBancaria("sandra Martinez", 348900,1200)
print(cuentaBancaria1.titular, cuentaBancaria1._saldo)
print(cuentaBancaria1.deposito(500000))
print(cuentaBancaria1.deposito(500000))
print(cuentaBancaria1.retirar(348900))
print(cuentaBancaria1.retirar(500000))
print(cuentaBancaria1.modificarClave(9999))
        
