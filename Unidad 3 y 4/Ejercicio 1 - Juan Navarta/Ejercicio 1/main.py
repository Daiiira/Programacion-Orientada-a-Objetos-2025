from gestorHotel import GestorHotel as GH

if __name__ == "__main__":
    hoteles = GH()

    hoteles.cargarArchivo()

    op1 = -1
    op2 = -1
    while op1 != 0:
        print("-- Sistema de Hoteles --\n" \
        "1- Ingresar Nombre de Hotel para Comenzar.\n" \
        "0- Terminar Programa\n")
        op1 = int(input("Ingrese opcion: "))
        if op1 == 1:
            h = input("Ingrese nombre del hotel: ")
            h = "hotel " + h
            nomHot = h
            h = hoteles.buscarHotel(h)
            while op2 != 0:
                print(f"\n-- Opciones {nomHot.title()} --\n" \
                "1- Agregar Habitaciones\n" \
                "2- Reservar Habitacion\n" \
                "3- Liberar Habitacion\n" \
                "4- Mostrar Numero y Piso de Habitaciones de un mismo tipo\n" \
                "5- Mostrar Cantidad de Habitaciones Libres en un Piso especifico\n" \
                "6- Para cada Tipo de Habitacion, mostrar detalles\n" \
                "0- Atras (nuevo hotel)\n")
                op2 = int(input("Ingrese opcion a elegir: "))
                if op2 == 1:
                    hoteles.agregarHabitacion(h)
                elif op2 == 2:
                    hoteles.reservarHabitacion(h)
                elif op2 == 3:
                    hoteles.liberarHabitacion(h)
                elif op2 == 4:
                    hoteles.mostrarPorTipo(h)
                elif op2 == 5:
                    hoteles.mostrarLibresPorPiso(h)
                elif op2 == 6:
                    hoteles.mostrarTodoPorTipo(h)
                elif op2 == 0:
                    print("Volviendo...")
                else:
                    print("Opcion Inexistente")
        elif op1 == 0:
            print("Saliendo del programa.")