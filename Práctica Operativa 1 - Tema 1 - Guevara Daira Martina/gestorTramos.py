import csv
from claseTramo import tramo

class gestorTramos:
    __lista = []

    def __init__(self):
        self.__lista = []

    def getLista(self):
        return self.__lista

    def cargaTramos(self):
        archivo = open('tramos.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            ciudadOrigen = fila[0]
            ciudadDestino = fila[1]
            distancia = int(fila[2])
            patente = fila[3]
            unTramo = tramo(ciudadOrigen, ciudadDestino, distancia, patente)
            self.__lista.append(unTramo)
        archivo.close()
        print("Tramos cargados correctamente.")

    def buscaTramos(self, patente):
        acum = 0
        print(f"\nTramos recorridos por el colectivo con patente {patente}:")
        for tramo in self.__lista:
            if tramo.getPatente() == patente:
                origen = tramo.getCiudadOrigen()
                destino = tramo.getCiudadDestino()
                dist = tramo.getDistancia()
                print(f" - De {origen} a {destino}: {dist} km")
                acum += dist
        print(f"\nDistancia total recorrida: {acum} km")
        
    def getDistMayor(self, dist):
        print("\nTramos con distancia mayor a", dist, "km:")
        for tramos in self.__lista:
            if tramos.getDistancia() > dist:
                print(tramos)