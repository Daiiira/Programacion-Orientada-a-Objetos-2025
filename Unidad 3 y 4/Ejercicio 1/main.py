#Agregar habitaciones al hotel.
#2. Reservar una habitación.
#3. Liberar una habitación.
#4. Dado un tipo de habitación (sencilla, doble, suite), mostrar número y piso de las
#habitaciones de ese tipo.
#5. Mostrar la cantidad de habitaciones libres por piso.
#6. Para cada tipo de habitación mostrar el detalle asociado con el siguiente formato:
#Tipo_de habitacion: xxxxxxxxxx
#Número piso Precio por noche Disponobilidad
#xxxxx xx xxx xxx
from gestorHotel import GestorHotel

if __name__ == "__main__":
    hotel = GestorHotel()
    hotel.cargarArchivo()

    while True:
        print("-- Sistema de Hoteles --\n" \
              "1- Ingresar Nombre de Hotel para Comenzar.\n" \
              "0- Terminar Programa\n")# Mostrar opciones
        op1 = int(input("Ingrese opcion: "))
        if op1 == 1:
            h = input("Ingrese nombre del hotel: ")
            h = "hotel " + h
            nomHot = h
            h = hotel.buscarHotel(h)
            while True:
                
            