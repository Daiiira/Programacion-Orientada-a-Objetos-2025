class Habitacion:
    __numero = int
    __piso = int
    __tipoHab = str             #sencilla, doble, suite
    __precioNoche = float
    __dispo = bool

    def __init__(self, numero, piso, tipoHab, precioNoche, dispo):
        self.__numero = numero
        self.__piso = piso
        self.__tipoHab = tipoHab
        self.__precioNoche = precioNoche
        self.__dispo = dispo

    def getNumero(self):
        return self.__numero
    def getPiso(self):
        return self.__piso
    def getTipo(self):
        return self.__tipoHab
    def getPrecio(self):
        return self.__precioNoche
    def getDisp(self):
        return self.__dispo
    
    def getDispFormat(self):
        disp = ""
        if self.__dispo == True:
            disp = "Disponible"
        elif self.__dispo == False:
            disp = "Reservada"
        return disp
    
    def setDisp(self, disp):
        self.__dispo = bool(disp)

    def __str__(self):
        cadena = 'Número de Habitación: {} Piso: {}\n'.format(self.__numero, self.__piso)
        cadena += 'Tipo de Habitación: {} Precio por noche: {}\n'.format(self.__tipoHab, self.__precioNoche)
        cadena += 'Disponibilidad: {}'.format(self.__dispo)
        return cadena