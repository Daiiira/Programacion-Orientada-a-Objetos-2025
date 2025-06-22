from ClaseMedio import Medio
class Television(Medio):
    __programas:list
    __cantidadprogramas:int
    __canal: int

    def __init__(self,nombre,canal,audiencia,cantidadprogramas):
        super().__init__(nombre,audiencia)
        self.__cantidadprogramas=cantidadprogramas
        self.__programas=[]
        self.__canal=canal
    
    def agregar(self,programa):
        self.__programas.append(programa)
    
    def mostrarprograma(self):
        for Programa in self.__programas:
            print(Programa) 
    def mostrarDatos(self):
        print(self)
        self.mostrarprograma()
    def getCantidadProgramas(self):
        return self.__cantidadprogramas
    def getCanal(self):
        return self.__canal
    def getListaP(self):
        return self.__programas
    def __str__(self):
        return (f"{super().__str__()}\nCANTIDAD DE PROGRAMAS:{self.__cantidadprogramas}\nCANAL:{self.__canal}")