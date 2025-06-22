from claseHabitacion import Habitacion
from claseHotel import Hotel
import csv

class GestorHoteles:
    __listaHoteles: list

    def __init__(self):
        self.__listaHoteles = []

    def agregaHotel(self, unHotel):
        self.__listaHoteles.append(unHotel)

    def agregaHab(self, nomb, num, piso, tipo, prec, disp):
        i = self.buscaPorNombre(nomb)
        self.__listaHoteles[i].agregaHabitacion(num, piso, tipo, prec, disp)
        self.__listaHoteles[i].ordenador()

    def buscaPorNombre(self, nom):
        i = 0
        encontrado = False
        while i< len(self.__listaHoteles) and not encontrado:
            if self.__listaHoteles[i].getNombre().lower() == nom.lower():
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError
        return i

    def inciso1(self, xnomb):
        indice = self.buscaPorNombre(xnomb)
        xnum = int(input("Ingrese el numero: "))
        xpiso = int(input("Ingrese piso: "))
        xtipo = input("Ingrese tipo: ")
        xprec = float(input("Ingrese precio por noche: "))
        self.__listaHoteles[indice].agregaHabitacion(xnum, xpiso, xtipo, xprec)
        self.__listaHoteles[indice].ordenador()
        print("Habitacion agregada.")
    
    def inciso2(self, xnom, xnum):
        indice = self.buscaPorNombre(xnom)
        subindice = self.__listaHoteles[indice].buscaPorNum(xnum)
        disponible = self.__listaHoteles[indice].getDispo(subindice)
        if disponible == True:
            self.__listaHoteles[indice].setDispo(subindice, 0)
            print(f"Habitación {xnum} reservada exitosamente anasheee.")
        else:
            print(f"Habitación {xnum} ya reservada.")

    def inciso3(self, xnom, xnum):
        indice = self.buscaPorNombre(xnom)
        subindice = self.__listaHoteles[indice].buscaPorNum(xnum)
        self.__listaHoteles[indice].setDispo(subindice, 1)
        print(f"Habitación {xnum} liberada.")

    def inciso4(self, xtipo):
        for hotel in self.__listaHoteles:
            hotel.muestraTipos(xtipo, hotel.getNombre())

    def inciso5(self):
        for hotel in self.__listaHoteles:
            hotel.muestraLibres()
        
    def inciso6(self):
        for tipo in ['doble','sencilla','suite']:
            print(f"Tipo de habitacion: {tipo}")
            for hotel in self.__listaHoteles:
                hotel.listaInfo(tipo)