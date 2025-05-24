from gestorCliente import gestorCliente
from gestorMovimiento import gestorMov

if __name__ == "__main__":
    cli = gestorCliente()
    mov = gestorMov()
    cli.cargarClientes()
    mov.cargarMov()

    while True:
        print("\nMenú de opciones: \n")
        print("a) Actualizar saldo de un cliente")
        print("b) Informar apellido y nombre de cliente (sin movimientos)")
        print("c) Ordenar Gestor de Movimientos por número de tarjeta")
        print("x) Salir")

        opcion = input("\nSeleccione una opción: ").lower()
        if opcion == 'a':
            dni = int(input("Ingrese el DNI del cliente: "))
            cli.actualizarSaldo(dni, mov)
        elif opcion == 'b':
            tarjeta = int(input("Ingrese el número de tarjeta: "))
            mov.clienteSinMovs(tarjeta, cli)
        elif opcion == 'c':
            mov.ordenarMovs()
            print("Gestor de Movimientos ordenado por número de tarjeta.")
        elif opcion == 'x':
            print("\nSaliendo del programa...")
            break
        else: 
            print("Opción no válida. Por favor, vuelva a intentarlo.")