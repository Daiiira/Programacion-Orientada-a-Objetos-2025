class beneficiario:
    __dni = int
    __nombre = str
    __apellido = str
    __carrera = str
    __facultad = str
    __año = int
    __promedio = float
    __idBecaAsig = int

    def __init__(self, dni, nombre, apellido, carrera, facultad, año, promedio, idBecaAsig):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__facultad = facultad
        self.__año = año
        self.__promedio = promedio
        self.__idBecaAsig = idBecaAsig

    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCarrera(self):
        return self.__carrera
    def getFacultad(self):
        return self.__facultad
    def getAño(self):
        return self.__año
    def getPromedio(self):
        return self.__promedio
    def getIdBecaAsig(self):
        return self.__idBecaAsig
    
    def __str__(self):
        return f"DNI: {self.__dni}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Carrera: {self.__carrera}, Facultad: {self.__facultad}, Año: {self.__año}, Promedio: {self.__promedio}, Id Beca Asignada: {self.__idBecaAsig}"
    
    def __lt__(self, other):
        return self.__facultad < other.getFacultad()