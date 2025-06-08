# NUMPY SE INSTALA EN EL MAIN
from manejadorCarrera import gestorCarrera
from manejadorFacultad import gestorFacultad

if __name__ == '__main__':
    carr = gestorCarrera()
    facu = gestorFacultad()

    while True:
        print("\n Menú de opciones: \n")
        print("a) Cargar los datos de las Facultades en un arreglo NumPy.")
        print("b) Cargar los datos de las Carreras en un arreglo NumPy.")
        print("c) ¿Donde se dicta una carrera?")
        print("d) Cantidad de carreras que se dictan en cada facultad.")
        print("e) Nombre y duración de las carreras que se dictan según una Facultad.")
        print("f) Mostrar todos los datos (carreras y facultades).")
        print("x) Salir")

        opcion = input("\nSeleccione una opción: ").lower()
        if opcion == 'a':
            facu.cargaFacultad()
        elif opcion == 'b':
            carr.cargaCarrera()
        elif opcion == 'c':
            nom = input("Ingrese nombre de la carrera que desea consultar: ")
            carr.muestraNombre(nom, facu)
        elif opcion == 'd':
            facu.muestraOferta(carr)
        elif opcion == 'e':
            nom = input("Ingrese nombre de la facultad que desea consultar: ")
            facu.muestraDuracion(carr, nom)
        elif opcion == 'f':
            facu.muestraOferta(carr)
            print("Datos de unidades académicas:\n")
            facu.muestraInfoTotal(carr)
        elif opcion == 'x':
            print("\nSaliendo del programa...")
            break
        else: 
            print("Opción no válida. Por favor, vuelva a intentarlo.")