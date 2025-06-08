import csv
import numpy as np
from claseColectivo import Colectivo
from gestorTramos import gestorTramos

class gestorColectivos:
    __arreglo = np.ndarray
    __dimension = int
    __cantidad = int
    __incremento = int

    def __init__(self, dim):
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__arreglo = np.empty(dim, dtype=object) 
    
    def agregaColectivo(self, unCole):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)
        self.__arreglo[self.__cantidad] = unCole
        self.__cantidad += 1
    
    def cargaColectivo(self):
        archivo = open('colectivos.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            patente = fila[0]
            marca = fila[1]
            modelo = fila[2]
            capacidad = int(fila[3])
            dni = int(fila[4])
            unCole = Colectivo(patente, marca, modelo, capacidad, dni)
            self.agregaColectivo(unCole)
        archivo.close()
        print("Colectivos cargados correctamente.")

    def getLen(self):
        return len(self.__arreglo)
    
    def buscaChofer(self, dni):
        i = 0
        bandera = False
        while i < self.__cantidad and not bandera:
            if self.__arreglo[i] is not None and self.__arreglo[i].getDNI() == dni:
                bandera = True
            else:
                i += 1
        if bandera:
            return self.__arreglo[i].getPatente()
        else:
            return None

    def muestraDatosCole(self, tramo):
        for i in range(self.__cantidad):
            cole = self.__arreglo[i]
            consumo = Colectivo.getConsumoProm()
            acum = 0
            for unTramo in tramo.getLista():
                if unTramo.getPatente() == cole.getPatente():
                    acum += unTramo.getDistancia()
            print(f"El colectivo {cole.getPatente()} recorrió un total de {acum} KM con un gasto de {consumo * acum} L de combustible")