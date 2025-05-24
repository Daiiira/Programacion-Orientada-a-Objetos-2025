import numpy as np
import csv
from claseCarrera import carrera

class gestorCarrera:
    __arreglo = np.ndarray
    __cantidad = int
    __dimension = int
    __incremento = int          #atributos para el arreglo

    def __init__(self, dim = 6):        #inicializamos el arreglo numpy
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__arreglo = np.empty(self.__dimension, dtype=carrera)

# Agrega elementos al arreglo
    def agregaCarrera(self, unaCarrera):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)     #Python por defecto verifica que no haya otras referencias activas al mismo array. Si encuentra referencias, lanza un error para proteger la memoria. refcheck=false desactiva esa verificación de seguridad, forzando el redimensionamiento.
        self.__arreglo[self.__cantidad] = unaCarrera
        self.__cantidad += 1

# CARGA ARREGLO NUMPY con 6 columnas ya que asi lo determina el csv
    def cargaCarrera(self):
        with open("Carreras.csv", encoding='latin1') as archivo: 
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Saltar encabezado
            for fila in reader:
                codigoCarrera = int(fila[0])
                nombre = fila[1]
                titulo = fila[2]
                duracion = fila[3]
                nivel = fila[4]
                codigoFacu = int(fila[5])
                nueva_carrera = carrera(codigoCarrera, titulo, nombre, nivel, duracion, codigoFacu)
                self.agregaCarrera(nueva_carrera)
        print("Carreras cargadas.")
        archivo.close()

    def muestraNombre(self, nom, gf):
        i = 0
        NoEncontrado = True
        while NoEncontrado and i < self.__cantidad:
            if (nom.lower() == self.__arreglo[i].getNombre().lower()):
                nombFacu = gf.dadordeNombre(self.__arreglo[i].getCodFacu())
                nombCar = self.__arreglo[i].getNombre()    #nombre de la carrera bien escrita
                NoEncontrado = False
            else:
                i += 1
        if NoEncontrado:
            print("No se encontró la carrera ingresada.")
        else:
            print(f"La carrera {nombCar} se dicta en la {nombFacu}.")
            
    def cantCarreras(self, id):
        cont = 0
        for i in range(self.__cantidad):
            if id == self.__arreglo[i].getCodFacu():
                cont += 1
                print(f"{self.__arreglo[i].getNombre()}")
        print(f"Total: {cont} carreras.")

    def muestraDatos(self, id):
        bandera = False
        for i in range(self.__cantidad):
            if id == self.__arreglo[i].getCodFacu():
                print(f"{self.__arreglo[i].getNombre()}")
                bandera = True
        if not bandera:
            print("No se registran carreras en esta Facultad")

    def ordenar(self, id):
        #se ordena sólo la parte del arreglo que está ocupada
        carreras_validas = self.__arreglo[:self.__cantidad]
        carreras_ordenadas = sorted(carreras_validas)
        for carrera in carreras_ordenadas:
            if id == carrera.getCodFacu():
                print(carrera)