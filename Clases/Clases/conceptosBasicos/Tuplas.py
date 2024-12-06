#las tuplas son inmutables no se pueden modificar los elementos 
paises=('Colombia', 'Mexico','Ecuador','Venezuela')
print(type(paises))
#tamaño
print(len(paises))
#pocicion especifica
print(paises[2])
#ultimo elemento de la lista
print(paises[-1])
#recorrer la lista 
for pais in paises:
    print(pais)
# inmutables no piedo ingresar en posicion especifica de debe convertir en lista 
paisesLista=list(paises)
print(type(paisesLista))
print(paisesLista)
#se incerta en la pocicion especifica 
paisesLista[1]="Argentina"
print(paisesLista)
#se pasa lista a tupla
paises = tuple(paisesLista)
print(type(paises))
print(paises)
#Las tuplas se usan para datos sencibles y no deben ser modificadas 
del paises ##elimina tupla



