from habitacion import Habitacion

class Hotel:
    __nom: str
    __dir: str
    __tel: str
    __listHab: list

    def __init__(self, nom, dir, tel):
        self.__nom = nom
        self.__dir = dir
        self.__tel = tel
        self.__listHab = []

    def agregarHabitacion(self, num, piso, tipo, precio, disp):
        i = 0
        xHabt = Habitacion(num, piso, tipo, precio, disp)
        igual = False
        while not igual and i < len(self.__listHab):
            if self.__listHab[i].getNum() != num:
                i += 1
            else:
                igual = True
        if not igual:
            self.__listHab.append(xHabt)
        elif igual:
            print("Esa habitacion ya existe, ingrese otra.")

    def ordenarHabitaciones(self):
        self.__listHab.sort()

    def mostrarHabit(self):
        for hab in self.__listHab:
            print(hab)

    def reservarHabitacion(self, num):
        found = False
        i = 0
        while not found and i < len(self.__listHab):
            if self.__listHab[i].getNum() != num:
                i += 1
            elif self.__listHab[i].getNum() == num:
                found = True
                if self.__listHab[i].getDisp() == False:
                    print("La habitacion ya esta reservada. Disculpe las molestias.")
                else:
                    self.__listHab[i].setDisp(False)
                    print("Reservacion realizada con exito.")

    def liberarHabitacion(self, num):
        found = False
        i = 0
        while not found and i < len(self.__listHab):
            if self.__listHab[i].getNum() != num:
                i += 1
            elif self.__listHab[i].getNum() == num:
                found = True
                if self.__listHab[i].getDisp() == True:
                    print("La habitacion ya esta liberada.")
                else:
                    self.__listHab[i].setDisp(True)
                    print("Liberacion realizada con exito.")

    def mostrarPorTipo(self, tipo):
        print("")
        for hab in self.__listHab:
            if hab.getTipo() == tipo:
                print(f"Habitacion: {hab.getNum()} - Piso {hab.getPiso()}")

    def mostrarLibresPorPiso(self, piso):
        print("")
        for hab in self.__listHab:
            if hab.getPiso() == piso:
                print(hab)

    def mostrarTodoPorTipo(self):
            print("\nTipo de Habitacion: Sencilla")
            print("")
            print(f"{"Numero":<15}{"Piso":<15}{"Precio":<15}{"Disponibilidad":<15}")
            for hab in self.__listHab:
                if hab.getTipo() == "sencilla":
                    print(f"{hab.getNum():<15}{hab.getPiso():<15}{hab.getPrecio():<15}{hab.getDispFormat():<15}")
            print("\nTipo de Habitacion: Doble")
            print("")
            print(f"{"Numero":<15}{"Piso":<15}{"Precio":<15}{"Disponibilidad":<15}")
            for hab in self.__listHab:
                if hab.getTipo() == "doble":
                    print(f"{hab.getNum():<15}{hab.getPiso():<15}{hab.getPrecio():<15}{hab.getDispFormat():<15}")
            print("\nTipo de Habitacion: Suite")
            print("")
            print(f"{"Numero":<15}{"Piso":<15}{"Precio":<15}{"Disponibilidad":<15}")
            for hab in self.__listHab:
                if hab.getTipo() == "suite":
                    print(f"{hab.getNum():<15}{hab.getPiso():<15}{hab.getPrecio():<15}{hab.getDispFormat():<15}")

    def getNom(self):
        return self.__nom

    def getDir(self):
        return self.__dir
    
    def getTel(self):
        return self.__tel
    
    def __str__(self):
        return f"{self.__nom} - {self.__dir}"