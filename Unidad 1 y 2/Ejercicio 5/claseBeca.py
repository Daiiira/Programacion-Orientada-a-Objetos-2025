class beca:
    __idBeca = int
    __tipoBeca = str            # (‘F’- Fotocopia, ‘T´-Transporte, ‘A’-Ayuda Económica)
    __montoBeca = float

    def __init__(self, idBeca, tipoBeca, montoBeca):
        self.__idBeca = idBeca
        self.__tipoBeca = tipoBeca
        self.__montoBeca = montoBeca
    
    def getIdBeca(self):
        return self.__idBeca
    def getTipoBeca(self):
        return self.__tipoBeca
    def getMontoBeca(self):
        return self.__montoBeca
    
    def __str__(self):
        return f'Id Beca: {self.__idBeca}, Tipo Beca: {self.__tipoBeca}, Monto Beca: ${self.__montoBeca}'