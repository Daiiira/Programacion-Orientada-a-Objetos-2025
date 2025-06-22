from claseHotel import Hotel
import csv

class GestorHotel:
    __listaHotel: list

    def __init__(self):
        self.__listaHotel = []

    def cargarArchivo(self):
        i = 0
        archivo = open('Hoteles.csv')
        reader = csv.reader(archivo, delimiter=';')
        for row in reader:
            if len(row) == 3:
                hotel = Hotel(row[0], row[1], row[2])
                self.__listaHotel.append(hotel)
                i += 1
            elif len(row) == 5:
                num = int(row[0])
                piso = int(row[1])
                tipo = row[2]
                precio = float(row[3])
                if row[4] == "True":
                    disp = True
                elif row[4] == "False":
                    disp = False
                self.__listaHotel[i-1].agregarHab(num, piso, tipo, precio, disp)
        archivo.close()
        print("Se cargaron los datos.")

    def agregarHab(self, i):
        bandera = True
        op = "s"
        while bandera:
            if op == "s":
                print("\nIngrese los datos de la habitacion. La disponibilidad siempre sera SI")
                num = int(input("Numero: "))
                piso = int(str(num)[0])
                tipo = input("Tipo: ")
                precio = float(input("Precio: "))
                disp = True
                self.__listaHotel[i].agregarHab(num, piso, tipo.lower(), precio, disp)
                op = input("Habitacion Cargada. ¿Desea continuar con la carga? (s/n): ")
                op = op.lower()
            elif op == "n":
                print("Fin.")
                bandera = False
    
    def reservarHab(self, i):
        band = True
        op = "s"
        while band:
            if op == "s":
                num = int(input("\nIngrese numero de habitacion a reservar: "))
                self.__listaHotel[i].reservarHab(num)
                op = input("¿Quiere realizar otra reserva? (s/n): ")
                op.lower()
            elif op == "n":
                print("Volviendo...")
                band = False
            else:
                print("Opcion Incorrecta.")
                op = input("¿Quiere liberar otra habitacion? (s/n)")
                op.lower()
    
    def liberarHab(self, i):
        band = True
        op = "s"
        while band:
            if op == "s":
                num = int(input("\nIngrese numero de habitacion a liberar: "))
                self.__listaHotel[i].liberarHab(num)
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
                op = input("¿Quiere buscar otro tipo de habitación? (s/n)")
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
                op = input("¿Quiere seleccionar otro piso? (s/n)")
                op.lower()