
#Clase 3: Estructuras de control de flujo.
userHasDNI=True
age= float(input("Ingresa el segundo número: "))
country= input("Ingresa el segundo número USA , GER o COL : ")

#Condicionales  If.
"""
if age>=21 and country =='USA':
    print('you can buy alchol in USA')
elif age>=16 and country =='GER':
    print('you can buy alchol in GER')
elif age>=18 and country =='COL':
    print('you can buy alchol in COL')
else:
    userHasDNI= False
    print('you can buy alchol')
"""
#Bucles básicos For.


for student in range(10):
    student+=1
    print(student)


#Bucles básicos While.
"""
studentNumber=0
while userHasDNI:
    studentNumber+=1
    if studentNumber==10:
        userHasDNI=False
    if age>=21 and country =='USA':
        print('you can buy alchol in USA')
        break
    elif age>=16 and country =='GER':
        print('you can buy alchol in GER')
        break
    elif age>=18 and country =='COL':
        print('you can buy alchol in COL')
        break
    else:
        print('you can´t buy alchol')
        break
"""