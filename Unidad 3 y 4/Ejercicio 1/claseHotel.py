from claseHabitacion import Habitacion

class Hotel:
    __nombre = str
    __direccion = str
    __telefono = str
    __listaHabitaciones = list

    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaHabitaciones = []
    
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono

    def agregarHabitacion(self, numero, piso, tipo, precio, disponible):
        i = 0
        unaHab = Habitacion(numero, piso, tipo, precio, disponible)
        igual = False
        while not igual and i < len(self.__listaHabitaciones):
            if self.__listaHabitaciones[i].getNumero() != numero:
                i += 1
            else:
                igual = True    
        if not igual:
            self.__listaHabitaciones.append(unaHab)
        elif igual:
            print("Habitación existente, reintente con otra habitación.")

    def reservaHab(self, numero):
        bandera = False
        i = 0
        while not bandera and i < len(self.__listaHabitaciones):
            if self.__listaHabitaciones[i].getNumero() != numero:
                i += 1
            elif self.__listaHabitaciones[i].getNumero() == numero:
                bandera = True
                if self.__listaHabitaciones[i].getDisp() == False:
                    print("La habitación ya está reservada.")
                else:
                    self.__listaHabitaciones[i].setDisp(False)
                    print("Reserva realizada con éxito.")

    def liberarHab(self, numero):
        bandera = False
        i = 0
        while not bandera and i < len(self.__listaHabitaciones):
            if self.__listaHabitaciones[i].getNumero() != numero:
                i += 1
            elif self.__listaHabitaciones[i].getNumero() == numero:
                bandera = True
                if self.__listaHabitaciones[i].getDisp() == True:
                    print("La habitación ya está liberada.")
                else:
                    self.__listaHabitaciones[i].setDisp(True)
                    print("Liberación realizada con éxito.")

    def mostrarTipo(self, tipo):
        i = 0
        cadena = 'Habitaciones de tipo {}:\n'.format(tipo)
        while i < len(self.__listaHabitaciones):
            if self.__listaHabitaciones[i].getTipo() == tipo:
                cadena += 'Número: {} Piso: {}\n'.format(self.__listaHabitaciones[i].getNumero(), self.__listaHabitaciones[i].getPiso())
            i += 1
        return cadena
    
    def mostrarHabsLibres(self, piso):
        acum = 0
        for habitacion in self.__listaHabitaciones:
            if habitacion.getPiso() == piso and habitacion.getDisp() == True:
                acum += 1
        if acum == 0:
            cadena += 'No hay habitaciones libres en este piso.'
        else:
            cadena = 'Habitaciones libres en el piso {}:\n'.format(piso)
            cadena += 'Número: {} Tipo: {}\n'.format(self.__listaHabitaciones[habitacion].getNumero(), self.__listaHabitaciones[habitacion].getTipo())
            cadena += 'Total de habitaciones libres: {}\n'.format(acum)
        return cadena
    
    def mostrarPorTipo(self):
        print("\nTipo de Habitación: Sencilla")
        print(f"{"Número":>5} {"Piso":>5} {"Precio":>10} {"Disponibilidad":>15}")
        for habitacion in self.__listaHabitaciones:
            if habitacion.getTipo() == 'sencilla':
                print(f"{habitacion.getNumero():>5} {habitacion.getPiso():>5} {habitacion.getPrecio():>10} {habitacion.getDispFormat():>15}")
        print("\nTipo de Habitación: Doble")
        print(f"{"Número":>5} {"Piso":>5} {"Precio":>10} {"Disponibilidad":>15}")
        for habitacion in self.__listaHabitaciones:
            if habitacion.getTipo() == 'doble':
                print(f"{habitacion.getNumero():>5} {habitacion.getPiso():>5} {habitacion.getPrecio():>10} {habitacion.getDispFormat():>15}")
        print("\nTipo de Habitación: Suite")
        print(f"{"Número":>5} {"Piso":>5} {"Precio":>10} {"Disponibilidad":>15}")
        for habitacion in self.__listaHabitaciones:
            if habitacion.getTipo() == 'suite':
                print(f"{habitacion.getNumero():>5} {habitacion.getPiso():>5} {habitacion.getPrecio():>10} {habitacion.getDispFormat():>15}")

    def __str__(self):    
        cadena = 'Hotel: \n'.format(self.__nombre)
        cadena += 'Direccion: {} Teléfono: {}'.format(self.__direccion, self.__telefono)
        cadena += '\nLista de Habitaciones:\n'
        for habitacion in self.__listaHabitaciones:
            cadena += str(habitacion) + '\n'
        return cadena