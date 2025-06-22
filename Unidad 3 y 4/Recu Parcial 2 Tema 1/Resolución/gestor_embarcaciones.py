from embarcacion import Embarcacion

class GestorEmbarcaciones:
    def __init__(self):
        self.__lista = []

    def agregarEmbarcacion(self, embarcacion):
        if not isinstance(embarcacion, Embarcacion):
            raise TypeError("El objeto no es una Embarcación")

        for e in self.__lista:
            if e.getNombre() == embarcacion.getNombre():
                raise ValueError("Ya existe una embarcación con ese nombre")

        self.__lista.append(embarcacion)

    def alquilarPorNombre(self, nombre):
        encontrado = False
        for embarcacion in self.__lista:
            if embarcacion.getNombre() == nombre:
                encontrado = True
                if embarcacion.estaDisponible():
                    embarcacion.alquilar()
                    print("Embarcación alquilada con éxito")
                else:
                    print("Embarcación no disponible")
        if not encontrado:
            print("Embarcación no encontrada")

    def mostrarAlquiladas(self):
        for embarcacion in self.__lista:
            embarcacion.mostrarAlquilada()

    def mostrarDisponibles(self):
        for embarcacion in self.__lista:
            if embarcacion.estaDisponible():
                tipo = type(embarcacion).__name__
                print(f"Nombre: {embarcacion.getNombre()} - Costo diario: ${embarcacion.getCostoDiario()} - Tipo: {tipo}", end="")

                if tipo == "Velero":
                    print(f" - Velas: {embarcacion.getCantVelas()}")
                elif tipo == "Lancha":
                    print(f" - Potencia: {embarcacion.getPotencia()} HP")
                else:
                    print()
