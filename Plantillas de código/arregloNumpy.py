import csv
import numpy as np
from claseX import claseX

class gestorArr:
    __arreglo = np.ndarray
    __dimension = int
    __cantidad = int
    __incremento = int

    def __init__(self, dim):
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__arreglo = np.empty(dim, dtype=object) 
    
    def agregaArr(self, unaX):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)
        self.__arreglo[self.__cantidad] = unaX
        self.__cantidad += 1
    
    def cargaArr(self):
        archivo = open('archivo.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            var1 = fila[0]
            var2 = fila[1]
            var3 = fila[2]
            var4 = int(fila[3])             #si lo que va a leer es un int o float, debo escribirlo antes del input
            var5 = int(fila[4])
            unaX = claseX(var1, var2, var3, var4, var5)
            self.agregaArr(unaX)
        archivo.close()
        print("Arreglo cargado correctamente.")

    def getLen(self):
        return len(self.__arreglo)