class Cliente:
    __nombre = str
    __apellido = str
    __dni = int
    __numero_tarjeta = int
    __saldo_anterior = float
    
    def __init__(self, nombre, apellido, dni, numero_tarjeta, saldo_anterior):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__numero_tarjeta = numero_tarjeta
        self.__saldo_anterior = saldo_anterior
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido 
    
    def getDni(self):   
        return self.__dni
    
    def getNumeroTarjeta(self):
        return self.__numero_tarjeta
    
    def getSaldoAnterior(self):
        return self.__saldo_anterior

    def __str__(self):
        return f"Cliente: {self.__nombre} {self.__apellido}, DNI: {self.__dni}, Tarjeta: {self.__numero_tarjeta}, Saldo Anterior: {self.__saldo_anterior}"    
