from claseDepto import departamento
from claseAccidente import accidente
from gestorDepto import gestorDepto

if __name__ == '__main__':
    control = gestorDepto()
    control.carga()
    accidente = accidente(control)

# Dado un numero de mes, mostrar para cada uno de los Departamentos: nombre del departamento y el total de accidentes ocurridos en el mes dado.
# Dado un mes, mostrar nombre de departamento y cantidad de accidentes, para el departamento que tuvo la mayor cantidad de accidentes.
# Dado el nombre de un departamento indicar la cantidad total de accidentes ocurridos el año anterior.
# Mostrar los datos registrados con el siguiente formato. La fila “TOTAL” se debe mostrar el total de accidentes del mes. 

# Menú de opciones
while True:
    print("\n Menú de opciones: \n")
    print("a) Ver la lista de los departamentos")
    print("b) Registrar accidentes por mes y departamento")
    print("c) Departamentos y accidentes por mes")
    print("d) Departamento con mayor cantidad de accidentes según un mes")
    print("e) Total de accidentes en el año anterior según un departamento")
    print("f) Mostrar los datos registrados")
    print("x) Salir")

    opcion = input("\nSeleccione una opción: ").lower()
    if opcion == 'a':
        control.mostrar()
    elif opcion == 'b':
        while True:
                nomDepto = input("Ingrese departamento (o 'fin' para volver): ")
                if nomDepto.lower() == 'fin':
                    break
                id_depto = control.obtener_id_por_nombre(nomDepto)
                if id_depto == -1:
                    print("Departamento no encontrado. Intente de nuevo.")
                    continue
                try:
                    mes = int(input("Mes (1 a 12): "))
                    cantidad = int(input("Cantidad de accidentes: "))
                except ValueError:
                    print("Debe ingresar números enteros. Reintente.")
                    continue
                accidente.carga(id_depto, mes, cantidad)
    elif opcion == 'c':
        mes = int(input("\nIngrese el mes a consultar, del 1 al 12: "))
        accidente.totalAccidentesMes(mes)
    elif opcion == 'd':
        unMes = int(input("\nIngrese el mes a consultar, del 1 al 12: "))
        accidente.mayorCantAccidentes(unMes)
    elif opcion == 'e':
        depto = (input("\nIngrese el nombre del departamento a consultar: "))
        accidente.totAccAnualesDepto(depto)
    elif opcion == 'f':
        accidente.mostrarTablaCompleta()
    elif opcion == 'x':
        print("\nSaliendo del programa...")
        break
    else:
        print("\nOpción no válida. Por favor, seleccione una opción válida.")