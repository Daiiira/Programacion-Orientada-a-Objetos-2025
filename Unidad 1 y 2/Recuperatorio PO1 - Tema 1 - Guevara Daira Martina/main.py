# Guevara Daira Martina - DNI 45885184 - Registro E010-311
from gestorMedicos import gestorMedicos
from gestorVisitas import gestorVisitas

if __name__ == "__main__":
    med = gestorMedicos()
    vis = gestorVisitas()
    med.cargaMedico()
    vis.cargaVisitas()

    while True:
            print("\nMenu de opciones:\n")
            print("a) Visitas realizadas por un médico según su DNI")   
            print("b) Listado de médicos e información de visitas")
            print("c) Visitas realizadas en una zona específica")
            print("x) Salir")

            opcion = input("\nSeleccione una opción: ").lower()
            if opcion == 'a':
                dni = int(input("Ingrese el DNI del médico que desea consultar: "))
                vis.visitasPorMedico(dni)
            elif opcion == 'b':
                med.infoMedicos(vis)
            elif opcion == 'c':
                zona = input("Ingrese la zona que desea consultar: ")
                vis.visitasPorZona(zona, med)
            elif opcion == 'x':
                print("Saliendo del programa...")
                break
            else: 
                print("Opción inválida. Intente nuevamente.")