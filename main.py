from estudiante import *
import csv

def ingresarDatos(n,estudiantes):
    for k in range(n):
        est = []
        nombre = input('Ingrese el nombre del estudiante: ').capitalize()
        est.append(nombre)
        cedula = int(input('ingrese la cedula del estudiante: '))
        est.append(cedula)
        nac = input('ingrese la decha de nacimiento del estudiante (dd/mm/aa): ')
        est.append(nac)
        sexo = input('Ingrese el sexo del estudiante (m/f): ').lower()
        est.append(sexo)
        carrera = input('Ingrese la carrera del estudiante: ').capitalize()
        est.append(carrera)
        estatura = float(input('Ingrese la estatura del estudiante: '))
        est.append(estatura)
        origen = input('Ingrese el origen del estudiante: ').capitalize()
        est.append(origen)
        estudiantes.append(est)

    filename = 'Datos.csv'
    try:
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            for item in estudiantes:
                writer.writerow([item[0],item[1],item[2],item[3],item[4],item[5],item[6]])
    except BaseException as e:
        print('BaseException:', filename)
    else:
        print('Los datos han sido guardados!!')
    return filename
def crearObjetos():
    objeto = []
    f = open("Datos.csv")
    reader = csv.reader(f)
    for row in reader:
        est = Estudiante(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        objeto.append(est)
    return objeto
def contadorSexo(objetos):
    listaM = []
    listaF = []
    for i in objetos:
        if i.sexo == 'f':
            listaF.append(i)
        else:
            listaM.append(i)
    return listaM, listaF
def edad(objetos):
    cont = 0
    for i in objetos:
        if not i.esMayorDeEdad():
            cont += 1
    print('\nLa cantidad de menores de edad es', cont)

baseEstudiantes = crearObjetos()
x = True
while x:
    m = input('-------Menu-------\n1. Desea agregar un nuevo estudiante\n2. Generar registro de estudiantes\n3. Equipos de Baloncesto\n4. Salir\nSeleccione su opcion: ')
    if m == '1':
        n = int(input('Ingrese la cantidad de estudiantes que desea ingresar: '))
        estudiantes = []
        ingresarDatos(n,estudiantes)
        baseEstudiantes = crearObjetos()
        print('\nDesea seleccionar otra opcion')
    elif m == '2':
        contm, contf = contadorSexo(baseEstudiantes)
        print('La cantidad de hombres es',len(contm),',la cantidad de mujeres es',len(contf), end='')
        edad(baseEstudiantes)
        print('\nDesea seleccionar otra opcion')
    elif m == '3':
        listaM, listaF = contadorSexo(baseEstudiantes)
        baloncestoM = []
        baloncestoF = []
        for i in listaF:
            if float(i.estatura) >= 1.70:
                baloncestoF.append(i)
        for i in listaM:
            if float(i.estatura) >= 1.80:
                baloncestoM.append(i)
        print('El equipo de hombres esta conformado por:\n')
        for i in baloncestoM:
            i.mostrar()
        print('El equipo de mujeres esta conformado por:\n')
        for i in baloncestoF:
            i.mostrar()
    elif m == '4':
        x = False

