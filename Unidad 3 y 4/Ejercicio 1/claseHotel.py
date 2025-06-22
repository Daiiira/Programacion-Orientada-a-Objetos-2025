from claseHabitacion import Habitacion

class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaHabitaciones: list

    def __init__(self, nom, dir, tel):
        self.__nombre = nom
        self.__direccion = dir
        self.__telefono = tel
        self.__listaHabitaciones = []

    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    
    def agregaHabitacion(self, num, piso, tipo, precio, dispon = True):
        self.__listaHabitaciones.append(Habitacion(num, piso, tipo, precio, dispon))
        
    def ordenador(self):
        self.__listaHabitaciones.sort()

    def buscaPorNum(self, num):
        i = 0
        encontrado = False
        while i < len(self.__listaHabitaciones) and not encontrado:
            if num == self.__listaHabitaciones[i].getNumero():
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError
        return i

    def getDispo(self, i):
        return self.__listaHabitaciones[i].getDisponibilidad()
    def setDispo(self, i, valor):
        self.__listaHabitaciones[i].setDisponibilidad(valor)

    def muestraTipos(self, tipo):
        print(f"Habitaciones con el tipo {tipo} en el {self.getNombre()}:")
        for habitacion in self.__listaHabitaciones:
            if habitacion.getTipoHab() == tipo:
                print(f"Número: {habitacion.getNumero()}. Piso: {habitacion.getPiso()}")

    def muestraLibres(self):
        print(f"- {self.getNombre()} -")
        for i in range(1,5):  # i representa el piso
            cant = 0
            for j in range(len(self.__listaHabitaciones)):
                if self.getDispo(j) and self.__listaHabitaciones[j].getPiso() == i:
                    cant += 1
            if cant > 1:
                print(f"Hay {cant} habitaciones disponibles en el piso {i}.")                
            elif cant == 1:
                print(f"Hay solo una habitacion disponible en el piso {i}.")
            else:
                print(f"No hay habitaciones disponibles en el piso {i}.")
    
    def listaInfo(self, tipo):
        for habitacion in self.__listaHabitaciones:
            if tipo == habitacion.getTipoHab():
                print(habitacion)