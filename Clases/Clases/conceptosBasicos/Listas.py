# listas-> diferentes tipos de datos 
nombres =['Juan','Sebastian','Melisa','Xiomara']
print(nombres)
print(type(nombres))
print(nombres[1])
print(nombres[-1]) #ultimo elemento de la lista -1
#punto de finalizacion siempre llega uno menos es un intervalo cerrado 
print(nombres[0:2])
print(nombres[:2]) # [:2] es igual [0:2]
print(len(nombres))
#agregar elemento al inicio
nombres.append('Elizabeth')
print(nombres)
#agregar en posicion espesifica
nombres.insert(1,'Maria')
print(nombres)
#eliminar
nombres.remove('Elizabeth')
print(nombres)
nombres.insert(1,'Elizabeth')
print(nombres)
#pop elimina el ultimo elemento de la lista 
nombres.pop()
print(nombres)
#eliminar con indice
del nombres[3]
print(nombres)
#pop elimina con pocicion 
nombres.pop(1)
print(nombres)
#limpiar la lista manteniendo la estructura 
nombres.clear()
print(nombres)
#Eliminar lista 
#del nombres
#print(nombres)