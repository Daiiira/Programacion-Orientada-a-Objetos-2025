import numpy as np
import csv
from claseMovimiento import Movimiento

class gestorMov:
    __arreglo = np.ndarray
    __cantidad = int
    __dimension = int
    __incremento = int          

    def __init__(self, dim = 5):       
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__arreglo = np.empty(self.__dimension, dtype=Movimiento)

    def getCantidad(self):
        return self.__cantidad
    
    def getMovimiento(self, indice):
        if 0 <= indice < self.__cantidad:
            return self.__arreglo[indice]
        else:
            print("Índice fuera de rango.")

    def agregaMov(self, unMov):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)
        self.__arreglo[self.__cantidad] = unMov
        self.__cantidad += 1

    def cargarMov(self):
        archivo = open('MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            numero_cuenta = int(fila[0])
            fecha = fila[1]
            descripcion = fila[2]
            tipo_movimiento = fila[3]
            importe = float(fila[4])
            mov = Movimiento(numero_cuenta, fecha, descripcion, tipo_movimiento, float(importe))
            self.agregaMov(mov)
        archivo.close()
        print("Movimientos cargados correctamente.")

    def clienteSinMovs(self, tarjeta, cli):
        i = 0
        encontrado = False
        while i < self.getCantidad():
            mov = self.getMovimiento(i)
            if mov.getNumeroCuenta() == tarjeta:
                print(f"Cliente con movimientos.")
                encontrado = True
                break
            i += 1
        if not encontrado:
            lista_clientes = cli.getLista()
            for cliente in lista_clientes:
                if cliente.getNumeroTarjeta() == tarjeta:
                    print(f"Cliente sin movimientos: {cliente.getNombre()} {cliente.getApellido()}")
                    return

    def ordenarMovs(self):
        self.__arreglo[:self.__cantidad] = np.sort(self.__arreglo[:self.__cantidad])
        print("\nMovimientos ordenados por número de cuenta:")
        for i in range(self.__cantidad):
            print(self.__arreglo[i])
