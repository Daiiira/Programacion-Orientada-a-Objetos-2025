from gestorBecas import gestorBecas
from gestorBeneficiarios import gestorBeneficiarios

if __name__ == "__main__":
    GBeca = gestorBecas()
    GBen = gestorBeneficiarios()
    GBeca.cargarBecas()
    GBen.cargarBeneficiarios()

    while True:
        print("\nMenú de opciones: \n")
        print("a) Lista de beneficiarios y monto total a abonar según una beca:")
        print("b) Nombre y apellido de beneficiario con más de una beca")
        print("c) Lista ordenada de beneficiarios")
        print("d) Nombre y apellido de estudiantes con promedio mayor a 8 y sin beca 'Ayuda Económica'")
        print("x) Salir")
        opcion = input("\nSeleccione una opción: ").lower()
        if opcion == 'a':
            tipoBeca = input("\nIngrese el tipo de la beca: ")
            GBeca.muestraListaTotal(tipoBeca, GBen)
        elif opcion == 'b':
            dni = int(input("\nIngrese el DNI del beneficiario a consultar: "))
            GBen.beneficiariosConMasDeUnaBeca(dni)
        elif opcion == 'c':
            GBen.listaOrdenada()
        elif opcion == 'd':
            GBen.estudiantesSinBeca()
        elif opcion == 'x':
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, vuelva a intentarlo.")