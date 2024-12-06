#los set no tienen pocicion se  busca por iteral NO permite duplicidad 
lenguajes ={'Java', 'JavaScript','Python'}
print(type(lenguajes))
print(lenguajes)
#tamaño
print(len(lenguajes))
# validar la existencia de un elemento
print('Go' in lenguajes)
print('Java' in lenguajes)
#adicionar elemento
lenguajes.add('Go')
print(lenguajes)

for lenguaje in lenguajes:
    print(lenguaje)

#se elimina con el iteral de informacion
lenguajes.remove('Java')
print(lenguajes)
#discard tambien elimina
lenguajes.discard('Python')
print(lenguajes)