from gestorGastos import gestorGas
from gestorMovilidades import gestorMov

if __name__ == '__main__':
    Mov = gestorMov()
    Gas = gestorGas()
    Mov.cargaMov()
    Gas.cargaGas()

    while True:
        print("\nMenú de opciones: \n")
        print("a) Listado de gastos del mes de Abril")
        print("b) Gastos y total a pagar según una fecha")
        print("c) Información de cada movilidad según una fecha")
        print("x) Salir")

        opcion = input("\nSeleccione una opción: ").lower()
        if opcion == 'a':
            pat = input("Ingrese la patente de una movilidad: ")
            Mov.muestraLista(pat, Gas)
        elif opcion == 'b':
            fecha = input("Ingrese la fecha que desea consultar (formato aaaa-mm-dd): ")
            Gas.totalGastosDia(fecha)
        elif opcion == 'c':
            fechaMov = input("Ingrese la fecha que desea consultar (formato aaaa-mm-dd): ")
            Gas.gastosPorFechaOrdenados(fechaMov, Mov)
        elif opcion == 'x':
            print("\nSaliendo del programa...")
            break
        else: 
            print("Opción no válida. Por favor, vuelva a intentarlo.")
                    