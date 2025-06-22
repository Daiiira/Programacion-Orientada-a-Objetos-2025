from ClaseMedio import Medio
class Prensa(Medio):
    __tipo:str
    __periodicidad:str

    def __init__(self,nombre,audiencia,tipo,periodicidad):
        super().__init__(nombre,audiencia)
        self.__tipo=tipo
        self.__periodicidad=periodicidad
    
    def mostrarDatos(self):
        print(self)
    def getTipo(self):
        return self.__tipo
    def getPeriodicidad(self):
        return self.__periodicidad
    
    def __str__(self):
        return (f"{super().__str__()}\nTIPO:{self.__tipo}\nPERIODICIDAD:{self.__periodicidad}")