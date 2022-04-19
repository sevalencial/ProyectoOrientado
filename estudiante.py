#Creando la clase estudiante
from datetime import *
from dateutil.relativedelta import relativedelta

class Estudiante():
    def __init__(self, nombre = '', cedula = 0, nac = '', sexo = '', carrera = '', estatura = 0.0, ciudad = ''):
        self._nombre = nombre
        self._cedula = cedula
        self._nac = nac
        self._sexo = sexo
        self._carrera = carrera
        self._estatura = estatura
        self._ciudad = ciudad

#Metodos Getters y Setters
    @property
    def nombre(self):
        return self._nombre
    @property
    def cedula(self):
        return self._cedula
    @property
    def nac(self):
        return self._nac
    @property
    def sexo(self):
        return self._sexo
    @property
    def carrera(self):
        return self._carrera
    @property
    def estatura(self):
        return self._estatura
    @property
    def ciudad(self):
        return self._ciudad
    
    @nombre.setter
    def nombre(self, nombre): 
        if nombre.isalpha():
            self._nombre = nombre
        else:
            print('no es valido')
    @cedula.setter
    def cedula(self, cedula):
        if cedula.isnumeric():
            self._cedula = cedula
        else:
            print('Entrada invalida')
    @nac.setter
    #Formato de fecha dd/mm/aa
    def nac(self, nac):
        try:
            datetime.strptime(nac, '%d/%m/%Y')
            self._nac = nac
        except ValueError:
            print("Fecha inválida")
    @sexo.setter
    def sexo(self, sexo):
        if sexo.isalpha():
            if len(sexo) == 1:
                self._sexo = sexo
            else:
                print('No es valido')
        else:
            print('No es valido')
    @carrera.setter
    def carrera(self, carrera):
        if carrera.isalpha():
            self._carrera = carrera
        else:
            print('no es valido')
    @estatura.setter
    def estatura(self, estatura):
        estatura = float(estatura)
        if isinstance(estatura, float):
            self._estatura = estatura
        else:
            print('No es valido')
        
    @ciudad.setter
    def ciudad(self, ciudad):
        if ciudad.isalpha():
            self._ciudad = ciudad
        else:
            print('no es valido')

    

    #Creando el metodo mostrar

    def mostrar(self):
        print('---------Datos Estudiante---------')
        print('Nombre:',self._nombre,'\nCedula:',self._cedula,'\nFecha de nacimiento:',self._nac,'\nSexo:',self._sexo,'\nCarrera:',self._carrera,'\nEstatura:',self._estatura,'\nOrigen:',self._ciudad)

    def esMayorDeEdad(self):
        year = self._nac.split('/')
        edad = relativedelta(datetime.now(), datetime(int(year[2]),int(year[1]),int(year[0])))
        if edad.years > 18:
            return True
        else:
            return False

laura = Estudiante('laura',1125683429,'02/02/1998','f','matematicas',1.64,'bogota')
laura.nac = '2000/01/31'
laura.mostrar()
