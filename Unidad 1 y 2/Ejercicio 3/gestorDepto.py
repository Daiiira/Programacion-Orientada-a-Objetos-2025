from claseDepto import departamento
import csv

# el menu debe contener las sig funcionalidades:
    # 1. Dado un mes del 1 al 12, mostrar para cada uno de los Departamentos: nombre y el total de accidentes ocurridos en el mes dado.
    # 2. Dado un mes, mostrar el nombre y cantidad de accidentes del departamento que tuvo la mayor cantidad de accidentes.
    # 3. Dado el nombre de un departamento indicar la cantidad total de accidentes ocurridos el año anterior (todos los meses). 

class gestorDepto:
    __lista = []

    def __init__(self):
        self.__lista = []

    def getLista(self):
        return self.__lista
    
    # funcion para leer los elementos del archivo y agregarlos a la lista
    def carga(self):
        archivo = open("Departamentos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)  # <-- Salta el encabezado
        for fila in reader:
            id = str(fila[0])
            nom = str(fila[1]) 
            self.__lista.append(departamento(id, nom))
        archivo.close()
    
    # funcion para mostrar (es recursiva)
    def mostrar(self):
        long = len(self.__lista)
        for i in range(long):
            self.__lista[i].mostrarDatos() #---> llama a la clase depto y muestra las instancias de esa clase una por una

    def obtener_id_por_nombre(self, nombre):
        for depto in self.__lista:
            if depto.getNombre().lower() == nombre.lower():
                return int(depto.getID())    # devuelve 1–19
        return -1