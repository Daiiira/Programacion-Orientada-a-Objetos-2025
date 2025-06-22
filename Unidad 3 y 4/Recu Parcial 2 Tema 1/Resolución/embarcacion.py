#ABC significa Abstract Base Class → te permite crear una clase que no puede ser instanciada directamente, solo puede ser heredada.
from abc import ABC, abstractmethod 
class Embarcacion(ABC):
    __nombre: str
    __eslora: float
    __anioFab: int
    __costoDiario: float
    __cantDias: int
    __disponible: bool    
    
    def __init__(self, nombre, eslora, anioFab, costoDiario, cantDias, disponible = True):
        self.__nombre = nombre
        self.__eslora = eslora
        self.__anioFab = anioFab
        self.__costoDiario = costoDiario
        self.__cantDias = cantDias
        self.__disponible = disponible

    def getNombre(self):
        return self.__nombre
    
    def getEslora(self):
        return self.__eslora

    def estaDisponible(self):
        return self.__disponible

    def getCostoDiario(self):
        return self.__costoDiario

    def getCantDias(self):
        return self.__cantDias

    def getAnio(self):
        return self.__anioFab
    
    def alquilar(self):  #a tener en cuenta
        self.__disponible = False

    #@abstractmethod se usa para definir métodos que deben ser implementados por las subclases sí o sí.
    @abstractmethod  #a tener en cuenta
    def calcularCostoTotal(self):
        pass

    def mostrarAlquilada(self):  #a tener en cuenta
        if not self.__disponible:
            print(f"Embarcación: {self.__nombre} - Costo Total: ${self.calcularCostoTotal()}")

    