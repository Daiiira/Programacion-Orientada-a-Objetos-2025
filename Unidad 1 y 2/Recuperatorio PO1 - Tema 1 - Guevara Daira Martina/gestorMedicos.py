# Guevara Daira Martina - DNI 45885184 - Registro E010-311
import csv
import numpy as np
from claseMedico import medico

class gestorMedicos:
    __arreglo = np.ndarray
    __dimension = int
    __cantidad = int
    __incremento = int

    def __init__(self, dim = 5):
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__arreglo = np.empty(dim, dtype=object) 
    
    def agregaMedico(self, med):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)
        self.__arreglo[self.__cantidad] = med
        self.__cantidad += 1
    
    def cargaMedico(self):
        archivo = open('medicos.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            dni = int(fila[0])
            nombre = fila[1]
            especialidad = fila[2]
            matricula = fila[3]
            zona = fila[4]
            med = medico(dni, nombre, especialidad, matricula, zona)
            self.agregaMedico(med)
        archivo.close()
        print("Archivo Medicos cargado correctamente.")

    def infoMedicos(self, vis):
        for i in range(self.__cantidad):
            cont = vis.visitasTotal(self.__arreglo[i].getDNI())
            print(f"Nombre: {self.__arreglo[i].getNombre()} - Especialidad: {self.__arreglo[i].getEspecialidad()} - Zona: {self.__arreglo[i].getZona()} - Total de Visitas: {cont} - Importe Total: ${cont * self.__arreglo[i].getValorVisita()}")
    
    def obtenerNombreMedico(self, zona):
        i = 0
        while i < self.__cantidad:
            if zona.lower() == self.__arreglo[i].getZona().lower():
                return self.__arreglo[i].getNombre()
            i += 1
        return None