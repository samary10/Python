estudiantes = []
cursos=['java','python']
docentes=[]
horarios=[]

#funcion para crear estudiante
def matricular_estud():
    nombre= input('Digite el nombre del estudiante: ')
    print('Seleccione el curso a matricular')
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')

    cursoSeleccionado = int(input('ingrese el numero del curso: '))
    if cursoSeleccionado >0 and cursoSeleccionado<=len(cursos):
        curso=cursos[cursoSeleccionado-1]
        estudiante={'nombre':nombre, 'curso':curso}
        estudiantes.append(estudiante)
        print(f'estudiante: {nombre}, matriculado en el curso: {curso}')
    else:
        print(f'El curso ingresado no es valido recuerde que hay {len(cursos)} cursos')

def asignarDocente():
    print('seleccione el curso al cual va a asignar el docente: ')
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    cursoSeleccionado = int(input('ingrese el numero del curso: '))
    if cursoSeleccionado>0 and cursoSeleccionado<=len(cursos):
        curso=cursos[cursoSeleccionado-1]
        nombreDocente=input('Ingrese el nombre del docente: ')
        docente={'nombre':nombreDocente, 'curso':curso}
        docentes.append(docente)
        print(f'Docente: {nombreDocente}, dictara el curso: {curso}')
    else:
        print(f'El curso ingresado no es valido recuerde que hay {len(cursos)} cursos')

# funcion para asignar horario
def asifnarHorario():
    print('seleccione es curso al cual desea asignar el horario: ')
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    cursoSeleccionado = int(input('ingrese el numero del curso: '))
    if cursoSeleccionado>0 and cursoSeleccionado<=len(cursos):
        curso=cursos[cursoSeleccionado-1]
        dias=input('Ingrese los dias de clase (ej: martes y jueves)')
        hora=input('ingrese la hora de la clase (ej: 6 pm )')
        horario={'curso':curso,'dias':dias, 'hora':hora}
        horarios.append(horario)
        print(f'El horario {horario} fue asignado al curso: {curso} los dias {dias}')
    else:
        print(f'El curso ingresado no es valido recuerde que hay {len(cursos)} cursos')

def mostrarEstudiantes():
    if estudiantes:
        print('Lista de estudiantes matriculados')
        for estudiante in estudiantes:
            print(f'Estudiante : {estudiante['nombre']}, Curso: {estudiante['curso']}')
        else:
            print('No hay estudiantes matriculados')

def mostrarDocentes():
    if estudiantes:
        print('Lista de docentes asignados')
        for docente in docentes:
            print(f'Docente: {docente['nombre']}, Curso: {docente['curso']}')
        else:
            print('No hay estudiantes matriculados')

def mostrarHorarios():
    if estudiantes:
        print('\nLista de horatios de los cursos')
        for horario in horarios:
            print(f'El curso: {horario['curso']}, se dicta : {horario['dias']}, en el horario {horario['hora']}')
        else:
            print('No hay horario asignado')

def editEstudiante():
    nombre=input('Ingrese El nombre del estudiante a editar:')
    for i,estudiante in estudiantes:
        if estudiante['nombre']==nombre:
            

while True:
    print('\n SISTEMA DE MATRICULAS DE DEV SENIOR')
    print('\n1. Matricular estudiante \n2. Asignar docente \n3. Asignar horario a un curso \n4. Lista de estudiantes matriculados ')
    print('5. Lista de docente asignados \n6. Lista de horarios de los cursos ')
    print('7. Editar Estudiante \n8. Eliminar Estudiante ')
    print('9. Cambiar Docente \n10. Modificar Horario \n11. Salir')
    opcion=int(input('digite la opcion: '))
    if opcion==1:
        matricular_estud()
    elif opcion==2:
        asignarDocente()
    elif opcion==3:
        asifnarHorario()
    elif opcion==4:
        mostrarEstudiantes()
    elif opcion==5:
        mostrarDocentes()
    elif opcion==6:
        mostrarHorarios()
    elif opcion==7:
        editEstudiante()
    elif opcion==8:
        deletEstudiantes()
    elif opcion==9:
        editDocente()
    elif opcion==10:
        editHorario()
    elif opcion==11:
        print('Gracias por usar el programa')
        break
    else: 
        print('Opcion no valida')