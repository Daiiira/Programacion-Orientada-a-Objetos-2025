from datetime import date

class carrera:
    __codigoCarrera = int
    __titulo = str
    __nombre = str
    __nivel = date
    __duracion = str
    __codigoFacu = int

    #inicializamos los atributos
    def __init__(self, codigoCarrera, titulo, nombre, nivel, duracion, codigoFacu):
        self.__codigoCarrera = codigoCarrera
        self.__titulo = titulo
        self.__nombre = nombre
        self.__nivel = nivel
        self.__duracion = duracion
        self.__codigoFacu = codigoFacu
    
    #con metodos getter para acceder a los atributos privados
    def getCodCarr(self):
        return self.__codigoCarrera
    def getTitulo(self):
        return self.__titulo
    def getNombre(self):
        return self.__nombre
    def getNivel(self):
        return self.__nivel
    def getDuracion(self):
        return self.__duracion
    def getCodFacu(self):
        return self.__codigoFacu
    
    #sobrecarga del operador __lt__ que sirve para ordenar de mayor a menor
    def __lt__(self, other):
        return self.getNombre() < other.getNombre()
    
    #funcion para mostrar datos
    def __str__(self):
        return f"Nombre de la carrera: {self.getNombre()}, Duracion: {self.getDuracion()}"
    
    #sobrecarga del operador __lt__ que es "menor que.."
    def __lt__(self, otra):
        return self.__nombre.lower() < otra.__nombre.lower()