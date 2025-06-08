# Los Movimientos: número de tarjeta, fecha, descripción, tipo de movimiento (‘C’ – Crédito, ‘P’-Pago) importe
class Movimiento:
    __numero_cuenta = int
    __fecha = str
    __descripcion = str
    __tipo_movimiento = str
    __importe = float

    def __init__(self, numero_cuenta, fecha, descripcion, tipo_movimiento, importe):
        self.__numero_cuenta = numero_cuenta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipo_movimiento = tipo_movimiento
        self.__importe = importe
    
    def getNumeroCuenta(self):
        return self.__numero_cuenta
    
    def getFecha(self):
        return self.__fecha
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getTipoMovimiento(self):
        return self.__tipo_movimiento
    
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"Tarjeta: {self.__numero_cuenta}, Fecha: {self.__fecha}, Descripción: {self.__descripcion}, Tipo: {self.__tipo_movimiento}, Importe: ${self.__importe}"
    
    def __lt__(self, otro):
        return self.__numero_cuenta < otro.getNumeroCuenta()