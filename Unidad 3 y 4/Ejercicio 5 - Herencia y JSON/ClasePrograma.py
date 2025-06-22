class Programa:
    __nombre:str
    __horainicio:str
    __horafin:str

    def __init__(self,nombre,horainicio,horafin):
        self.__nombre=nombre
        self.__horainicio=horainicio
        self.__horafin=horafin

    def getNombre(self):
        return self.__nombre
    def getHorainicio(self):
        return self.__horainicio
    def getHorafin(self):
        return self.__horafin
    
    def __str__(self):
        return (f"\n---PROGRAMA---\nNOMBRE:{self.__nombre}\nHORA INICIO:{self.__horainicio}\nHORA FIN:{self.__horafin}")
    