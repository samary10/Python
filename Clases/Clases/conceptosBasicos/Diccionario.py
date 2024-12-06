# conformado por una clave y un valor la clave puede ser alfabetica o numeroca
conceptosProgramacion={'POO':'Programacion Orientada a Obgetos',
                       'IDE': 'Entorno de desarrollo integrado',
                       'DBMS':'Sistemas Gestor de BD'
                       }
print(type(conceptosProgramacion))
print(conceptosProgramacion)
#numero de elementos
print(len(conceptosProgramacion))
#llamar elemento del diccionario
print(conceptosProgramacion['IDE'])
#optener con get
print(conceptosProgramacion.get('POO'))
#modificar elementos 
conceptosProgramacion['DBMS']='Database Managment System'
print(conceptosProgramacion)
#imprimir id de diccionario 
for key,value in conceptosProgramacion.items():#item pernite traer el valor 
    print(key,'->',value)