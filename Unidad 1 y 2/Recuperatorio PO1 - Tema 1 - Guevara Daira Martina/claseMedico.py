# Guevara Daira Martina - DNI 45885184 - Registro E010-311

class medico:
    __dni = int
    __nombre = str
    __especialidad = str
    __matricula = str
    __zona = str
    __valorVisita = 14500

    def __init__(self, dni, nombre, especialidad, matricula, zona):
        self.__dni = dni
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__matricula = matricula
        self.__zona = zona

    def getDNI(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getEspecialidad(self):
        return self.__especialidad
    def getMatricula(self):
        return self.__matricula
    def getZona(self):
        return self.__zona
    
    @classmethod
    def getValorVisita(cls):
        return cls.__valorVisita
    
    def __str__(self):
        return f"DNI: {self.__dni} - Nombre: {self.__nombre} - Especialidad: {self.__especialidad} - Matricula: {self.__matricula} - Zona: {self.__zona} - Valor Visita: {self.__valorVisita}"
    
    def __eq__(self, otro):
        return self.__zona == otro.getZona()