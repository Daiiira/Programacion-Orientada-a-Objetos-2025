from gestor_embarcaciones import GestorEmbarcaciones
from velero import Velero
from lancha import Lancha

def mostrarMenu():
    print(""" --- Menú de opciones ---
    1. Agregar embarcación
    2. Alquilar embarcación
    3. Mostrar embarcaciones alquiladas
    4. Mostrar embarcaciones disponibles
    0. Salir
""")

def main():
    gestor = GestorEmbarcaciones()
    salir = False

    while not salir:
        mostrarMenu()
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            tipo = input("Tipo (V para Velero / L para Lancha): ").upper() #usamos mayúsculas para que coincida con lo que ingres el usuario

            if tipo == "V" or tipo == "L":
                nombre = input("Nombre: ")
                eslora = float(input("Eslora (en metros): "))
                anio = int(input("Año de fabricación: "))
                dias = int(input("Cantidad de días: "))

                if tipo == "V":
                    velas = int(input("Cantidad de velas: "))
                    embarcacion = Velero(nombre, eslora, anio, dias, velas)
                else:
                    potencia = int(input("Potencia del motor en HP: "))
                    embarcacion = Lancha(nombre, eslora, anio, dias, potencia)

                try:
                    gestor.agregarEmbarcacion(embarcacion)
                    print("--- Embarcación agregada con éxito ---")
                except (TypeError, ValueError) as error:
                    print(f"Error: {error}")
            else:
                print("Tipo inválido.")

        elif opcion == "2":
            nombre = input("Nombre de la embarcación a alquilar: ")
            gestor.alquilarPorNombre(nombre)

        elif opcion == "3":
            print("\n---- Embarcaciones alquiladas ----")
            gestor.mostrarAlquiladas()

        elif opcion == "4":
            print("\n---- Embarcaciones disponibles ---- ")
            gestor.mostrarDisponibles()

        elif opcion == "0":
            salir = True

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
    
'''
Lote de prueba
1
V
La Gala
12.5
2022
3
2
1
L
Tiburón
9.8
2023
4
150
1
V
La Brisa
10.0
2020
2
3
2
Tiburón
1
La brisa
4
5
'''