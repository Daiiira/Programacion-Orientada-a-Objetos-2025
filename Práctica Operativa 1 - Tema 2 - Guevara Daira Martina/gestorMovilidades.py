import numpy as np
import csv
from claseMovilidad import Movilidad

class gestorMov:
    __arreglo = np.ndarray
    __cantidad = int
    __dimension = int
    __incremento = int          

    def __init__(self, dim = 6):       
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__arreglo = np.empty(self.__dimension, dtype=Movilidad)

    def agregaMov(self, unMov):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = unMov
        self.__cantidad += 1

    def cargaMov(self):
        with open("movilidades.csv") as archivo: 
            reader = csv.reader(archivo, delimiter=';')
            next(reader) 
            for fila in reader:
                patente = fila[0]
                tipo = fila[1]
                capacidadMov = fila[2]
                importeMov = fila[3]
                marca = fila[4]
                modelo = fila[5]
                mov = Movilidad(patente, tipo, float(capacidadMov), float(importeMov), marca, modelo)
                self.agregaMov(mov)
        archivo.close()

    def muestraLista(self, pat, gestorGas):
        i = 0
        NoEncontrado = True
        while NoEncontrado and i < self.__cantidad:                 # busca la patente que indica el usuario con algun match en el arreglo iterando indice por indice
            if pat.lower() == self.__arreglo[i].getPatenteMov().lower():
                mov = self.__arreglo[i]
                NoEncontrado = False
            else:
                i += 1
        if NoEncontrado:
            print("No se encontró la movilidad ingresada.")
            return

        print(f"Patente: {mov.getPatenteMov()} Tipo: {mov.getTipoMov()} Capacidad de Carga: {mov.getCapacidadMov()}")
        print(f"Importe Mensual de Patente: {mov.getImporteMov()} Marca: {mov.getMarca()} Modelo: {mov.getModelo()}")
        print("\nGastos\nFecha           Importe       Descripción")

        total = mov.getImporteMov()
        for gasto in gestorGas.getLista():
            if gasto.getPatente().lower() == pat.lower():           # busca el gasto asociado a esa patente
                print(f"{gasto.getFecha():<15}{gasto.getImporte():<13}{gasto.getDescripcion()}")
                total += float(gasto.getImporte())

        print(f"\nTotal de Gastos (incluye Patente): {total}")
    
    def buscarMovPorPatente(self, patente):
        for i in range(self.__cantidad):
            if self.__arreglo[i].getPatenteMov().lower() == patente.lower():
                return self.__arreglo[i]
        return None

