from hotel import Hotel
import csv

class GestorHotel:
    __listaHotel: list

    def __init__(self):
        self.__listaHotel = []

    def cargarArchivo(self):
        i = 0
        with open("F:/.Programación/.Programas/Python/POO 2025/Unidad 3/CSV/Hoteles.csv") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if len(row) == 3:
                    xHotel = Hotel(row[0], row[1], row[2])
                    self.__listaHotel.append(xHotel)
                    i += 1
                elif len(row) == 5:
                    num = int(row[0])
                    piso = int(row[1])
                    tipo = row[2]
                    precio = float(row[3])
                    #"Casteamos" de forma diferente, porque al usar el casteo nativo, todos los datos pasan a ser True.
                    if row[4] == "True":
                        disp = True
                    elif row[4] == "False":
                        disp = False
                    self.__listaHotel[i-1].agregarHabitacion(num, piso, tipo, precio, disp)

    def buscarHotel(self, hotel):
        found = False
        i = 0
        op = "s"
        while not found and i < len(self.__listaHotel):
            if self.__listaHotel[i].getNom() == hotel.title():
                found = True
            else:
                i += 1
        if i >= len(self.__listaHotel):
            print("No se encontro el hotel.")
        elif found == True:
            return i
    def agregarHabitacion(self, i):
        band = True
        op = "s"
        while band:
            if op == "s":
                print("\nIngrese los datos de la habitacion. La disponibilidad siempre sera SI")
                num = int(input("Numero: "))
                piso = int(str(num)[0])
                tipo = input("Tipo: ")
                precio = float(input("Precio: "))
                disp = True
                self.__listaHotel[i].agregarHabitacion(num, piso, tipo.lower(), precio, disp)
                op = input("Habitacion Cargada! ¿Quieres Cargar Otra? (s/n): ")
                op.lower()
            elif op == "n":
                self.__listaHotel[i].ordenarHabitaciones()
                print("Volviendo...")
                band = False
            else:
                print("Opcion Incorrecta.")
                op = input("¿Quiere liberar otra habitacion? (s/n)")
                op.lower()

    def reservarHabitacion(self, i):
        band = True
        op = "s"
        while band:
            if op == "s":
                num = int(input("\nIngrese numero de habitacion a reservar: "))
                self.__listaHotel[i].reservarHabitacion(num)
                op = input("¿Quiere realizar otra reserva? (s/n): ")
                op.lower()
            elif op == "n":
                print("Volviendo...")
                band = False
            else:
                print("Opcion Incorrecta.")
                op = input("¿Quiere liberar otra habitacion? (s/n)")
                op.lower()

    def liberarHabitacion(self, i):
        band = True
        op = "s"
        while band:
            if op == "s":
                num = int(input("\nIngrese numero de habitacion a liberar: "))
                self.__listaHotel[i].liberarHabitacion(num)
                op = input("¿Quiere liberar otra habitacion? (s/n): ")
                op.lower()
            elif op == "n":
                print("Volviendo...")
                band = False
            else:
                print("Opcion Incorrecta.")
                op = input("¿Quiere liberar otra habitacion? (s/n)")
                op.lower()

    def mostrarPorTipo(self, i):
        band = True
        op = "s"
        while band:
            if op == "s":
                tipo = input("\nIngrese el tipo de habitacion a buscar: ")
                tipo.lower()
                self.__listaHotel[i].mostrarPorTipo(tipo)
                op = input("¿Quiere elegir otro tipo? (s/n): ")
            elif op == "n":
                print("Volviendo...")
                band = False
            else:
                print("Opcion Incorrecta.")
                op = input("¿Quiere liberar otra habitacion? (s/n)")
                op.lower()

    def mostrarLibresPorPiso(self, i):
        band = True
        op = "s"
        while band:
            if op == "s":
                piso = int(input("Ingrese un piso: "))
                self.__listaHotel[i].mostrarLibresPorPiso(piso)
                op = input("¿Quiere revisar otro piso? (s/n): ")
                op.lower()
            elif op == "n":
                print("Volviendo...")
                band = False
            else:
                print("Opcion Incorrecta.")
                op = input("¿Quiere liberar otra habitacion? (s/n)")
                op.lower()

    def mostrarTodoPorTipo(self, i):
        self.__listaHotel[i].mostrarTodoPorTipo()