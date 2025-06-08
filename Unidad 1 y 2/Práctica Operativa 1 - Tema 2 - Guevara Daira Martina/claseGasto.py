class Gasto:
    __patenteGas = str
    __fecha = str
    __importe = float
    __descripcion = str

    def __init__(self, patenteGas, fecha, importe, descripcion):
        self.__patenteGas = patenteGas
        self.__fecha = fecha
        self.__importe = importe
        self.__descripcion = descripcion
    
    def getPatente(self):
        return self.__patenteGas
    
    def getFecha(self):
        return self.__fecha
    
    def getImporte(self):
        return self.__importe
    
    def getDescripcion(self):
        return self.__descripcion
    
    def __str__(self):
        return f"{self.__patenteGas, self.__fecha, self.__importe, self.__descripcion}"
    
    def __lt__(self, otro):
        return (self.__fecha, self.__patenteGas) < (otro.getFecha(), otro.getPatente())
