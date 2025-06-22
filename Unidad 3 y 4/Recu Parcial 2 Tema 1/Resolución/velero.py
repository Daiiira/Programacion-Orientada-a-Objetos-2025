from embarcacion import Embarcacion

class Velero(Embarcacion):
    def __init__(self, nombre, eslora, anio_fabricacion, cant_dias, cant_velas):
        super().__init__(nombre, eslora, anio_fabricacion, 200000, cant_dias)
        self.__cant_velas = cant_velas

    def calcularCostoTotal(self):
        return (self.getCostoDiario() + self.__cant_velas * 20000) * self.getCantDias()

    def getCantVelas(self):
        return self.__cant_velas
