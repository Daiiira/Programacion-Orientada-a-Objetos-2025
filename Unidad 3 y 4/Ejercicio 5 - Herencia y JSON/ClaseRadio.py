from ClaseMedio import Medio
class Radio(Medio):
    __emisora:str
    __frecuencia:str
    __programas:list

    def __init__(self,nombre,audiencia,emisora,frecuencia):
        super().__init__(nombre,audiencia)
        self.__emisora=emisora
        self.__frecuencia=frecuencia
        self.__programas=[]

    def agregar(self,programa):
        self.__programas.append(programa)
    def mostrarprograma(self):
        for Programa in self.__programas:
            print(Programa) 
    def mostrarDatos(self):
        print(self)
        self.mostrarprograma()
    def getFrecuencia(self):
        return self.__frecuencia
    def getEmisora(self):
        return self.__emisora
    def getListaP(self):
        return self.__programas
    
    def __str__(self):
        return (f"{super().__str__()}\nFRECUENCIA:{self.__frecuencia}")