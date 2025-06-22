class Habitacion:
    __numero: int
    __piso: int
    __tipoHab: str
    __precioNoche: float
    __disponibilidad: bool

    def __init__(self, num, piso, tipo, precio, dispo):
        self.__numero = num
        self.__piso = piso
        self.__tipoHab = tipo
        self.__precioNoche = precio
        self.__disponibilidad = dispo

    def getNumero(self):
        return self.__numero
    def getPiso(self):
        return self.__piso
    def getTipoHab(self):
        return self.__tipoHab
    def getPrecioNoche(self):
        return self.__precioNoche

    def setDisponibilidad(self, valor):
        if valor == 0:
            self.__disponibilidad = False
        else:
            self.__disponibilidad = True
    def getDisponibilidad(self):
        return self.__disponibilidad
    
    def __lt__(self, otro):
        return self.getNumero() < otro.getNumero()

    def __str__(self):
        if self.getDisponibilidad() == True:
            dispo = 'Disponible'
        else:
            dispo = 'Indisponible'
        return f"{self.getNumero()} - {self.getPiso()} - {self.getPrecioNoche()} - {dispo}"