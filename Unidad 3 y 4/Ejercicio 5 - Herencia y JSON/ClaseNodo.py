class Nodo:
    __dato:None
    __siguiente:None

    def __init__(self,medio):
        self.__dato=medio
        self.__siguiente=None

    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__dato
    def setSiguiente(self,nodo):
        self.__siguiente=nodo