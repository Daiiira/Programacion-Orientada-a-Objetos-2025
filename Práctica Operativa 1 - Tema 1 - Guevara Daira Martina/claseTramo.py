class tramo:
    __ciudadOrigen = str
    __ciudadDestino = str
    __distancia = int
    __patente = str

    def __init__(self, ciudadOrigen, ciudadDestino, distancia, patente):
        self.__ciudadOrigen = ciudadOrigen
        self.__ciudadDestino = ciudadDestino
        self.__distancia = distancia
        self.__patente = patente
    
    def getCiudadOrigen(self):
        return self.__ciudadOrigen
    def getCiudadDestino(self):
        return self.__ciudadDestino
    def getDistancia(self):
        return self.__distancia
    def getPatente(self):
        return self.__patente
    
    def __str__(self):
        return f'Ciudad Origen: {self.__ciudadOrigen}, Ciudad Destino: {self.__ciudadDestino}, Distancia: {self.__distancia}, Patente: {self.__patente}'

    def __gt__(self, otro):
        return self.__distancia > otro.getDistancia()