class Movilidad:
    __patenteMov = str
    __tipoMov = str         #(‘C’-Camión, ‘A’-Camioneta)
    __capacidadMov = float
    __importeMov = float
    __marca = str
    __modelo = str

    def __init__(self, patenteMov, tipoMov, capacidadMov, importeMov, marca, modelo):
        self.__patenteMov = patenteMov
        self.__tipoMov = tipoMov
        self.__capacidadMov = capacidadMov
        self.__importeMov = importeMov
        self.__marca = marca
        self.__modelo = modelo

    def getPatenteMov(self):
        return self.__patenteMov
    
    def getTipoMov(self):
        return self.__tipoMov
    
    def getCapacidadMov(self):
        return self.__capacidadMov

    def getImporteMov(self):
        return self.__importeMov
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def __str__(self):
        return f"Patente: {self.__patenteMov}, Tipo: {self.__tipoMov}, Capacidad: {self.__capacidadMov}, Importe: {self.__importeMov}, Marca: {self.__marca}, Modelo: {self.__modelo}"      