class Medio:
    __nombre:str
    __audiencia:int

    def __init__(self,nombre,audicencia):
        self.__nombre=nombre
        self.__audiencia=audicencia

    def getNombre(self):
        return self.__nombre
    def getAudiencia(self):
        return self.__audiencia
    def __str__(self):
        return (f"\n--MEDIO--\nNOMBRE:{self.__nombre}\nAUDIENCIA:{self.__audiencia}")