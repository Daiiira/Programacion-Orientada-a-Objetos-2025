import numpy as np
import csv
from claseFacultad import facultad

class gestorFacultad:
    __arreglo = np.ndarray
    __cantidad = int
    __dimension = int
    __incremento = int          #atributos para el arreglo

    def __init__(self, dim = 5):        #inicializamos el arreglo numpy
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__arreglo = np.empty(self.__dimension, dtype=facultad)

# Agregar elementos al arreglo
    def agregarFacultad(self, unaFacultad):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)
        self.__arreglo[self.__cantidad] = unaFacultad
        self.__cantidad += 1

# CARGA ARREGLO NUMPY con 6 columnas ya que asi lo determina el csv
    def cargaFacultad(self):
        with open("Facultades.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Salta la primera fila (encabezado)
            for fila in reader:
                codFacu = int(fila[0])           # Código de la facultad (entero)
                nomFacu = fila[1]                # Nombre (string)
                direccion = fila[2]              # Dirección (string)
                localidad = fila[3]              # Localidad (string)
                telefono = (fila[4])          # Teléfono (entero)
                nueva_facultad = facultad(codFacu, nomFacu, direccion, localidad, telefono)
                self.agregarFacultad(nueva_facultad)
        print("Facultades cargadas.")
        archivo.close()
    
    def dadordeNombre(self, unID):
        for i in range(self.__cantidad):
            if self.__arreglo[i].getCodFacu() == unID:
                return self.__arreglo[i].getNomFacu()
        return "ID de facultad no encontrado"
    
    def muestraOferta(self, gc):
        for i in range(self.__cantidad):
            print(f"Para la {self.__arreglo[i].getNomFacu()}:")
            gc.cantCarreras(self.__arreglo[i].getCodFacu())
            print("")

    def muestraInfoTotal(self, gc):
        for i in range(self.__cantidad):
            print(f"Para la {self.__arreglo[i].getNomFacu()}:")
            gc.muestraDatos(self.__arreglo[i].getCodFacu())
            print("")
    
    def muestraDuracion(self, gc, nom):
        i = 0
        bandera = True
        while i < self.__cantidad and bandera:
            if self.__arreglo[i].getNomFacu().lower() == nom.lower():
                bandera = False
                print(f"Para la {self.__arreglo[i].getNomFacu()}:")
                gc.ordenar(self.__arreglo[i].getCodFacu())
            else:
                i += 1
        if bandera:
            print(f"\nNo se encontró la facultad {nom}.")