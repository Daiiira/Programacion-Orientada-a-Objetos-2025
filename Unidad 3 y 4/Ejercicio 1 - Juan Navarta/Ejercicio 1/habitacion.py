class Habitacion:
    __num: int
    __piso: int
    __tipo: str
    __precio: float
    __disp: bool

    def __init__(self, num, piso, tipo, precio, disp):
        self.__num = num
        self.__piso = piso
        self.__tipo = tipo
        self.__precio = precio
        self.__disp = disp

    def __str__(self):
        xdis = ""
        if self.__disp == True:
            xdis = "Si"
        else:
            xdis = "No"
        return f"Num: {self.__num} - Piso: {self.__piso} - Tipo: {self.__tipo} - Precio: ${self.__precio} - Disponibilidad {xdis}"

    def getNum(self):
        return self.__num
    
    def getPiso(self):
        return self.__piso
    
    def getTipo(self):
        return self.__tipo
    
    def getPrecio(self):
        return self.__precio
    
    def getDisp(self):
        return self.__disp
    
    def getDispFormat(self):
        xdis = ""
        if self.__disp == True:
            xdis = "Disponible"
        elif self.__disp == False:
            xdis = "Reservada"
        return xdis
    
    def setDisp(self, xdis):
        self.__disp = bool(xdis)
    
    def __lt__(self, otraHabitacion):
        return self.__num < otraHabitacion.getNum()