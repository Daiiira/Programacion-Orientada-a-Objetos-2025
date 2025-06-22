from embarcacion import Embarcacion

class Lancha(Embarcacion):
    def __init__(self, nombre, eslora, anio_fabricacion, cant_dias, potencia):
        super().__init__(nombre, eslora, anio_fabricacion, 300000, cant_dias)
        self.__potencia = potencia

    def calcularCostoTotal(self):
        return (self.getCostoDiario() + self.__potencia * 5000) * self.getCantDias()

    def getPotencia(self):
        return self.__potencia
