from gestorColectivos import gestorColectivos
from gestorTramos import gestorTramos

if __name__ == "__main__":
    dim = int(input("Ingrese cantidad de colectivos: "))
    dim+=1
    cole = gestorColectivos(dim)
    tram = gestorTramos()

    cole.cargaColectivo()
    tram.cargaTramos()

    while True:
        print("\nMenu de opciones:\n")
        print("a) Tramos recorridos por un chofer (con DNI)")
        print("b) Cantidad de km recorridos y gasto de combustible por colectivo")
        print("c) Listar tramos con km recorridos mayores a una distancia dada")
        print("x) Salir")

        opcion = input("\nSeleccione una opción: ").lower()
        if opcion == 'a':
            dni = int(input("Ingrese el DNI del chofer: "))
            patente = cole.buscaChofer(dni)
            if patente is not None:
                tram.buscaTramos(patente)
            else:
                print("Chofer no encontrado.")
        elif opcion == 'b':
            cole.muestraDatosCole(tram)
        elif opcion == 'c':
            distancia = float(input("Ingrese la distancia en km: "))
            tram.getDistMayor(distancia)
        elif opcion == 'x':
            print("Saliendo del programa...")
            break
        else: 
            print("Opción inválida. Intente nuevamente.")