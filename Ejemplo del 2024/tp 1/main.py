from claseCliente import gestorCliente
from claseMov import Movimiento
from claseMov import gestorMov

if __name__ == '__main__':
  GestorCli = gestorCliente()
  GestorCli.cargarCliente()
  GestorCli.mostrar()
  
  GestorMov = gestorMov()
  GestorMov.cargarMov()
  GestorMov.mostrar()

# Menú de opciones
while True:
    print("\n Menú de opciones: \n")
    print("a) Actualizar saldo con DNI")
    print("b) Verificar movimientos con número de tarjeta")
    print("c) Ordenar movimientos según número de tarjeta")
    print("x) Salir")

    opcion = input("Seleccione una opción: ").lower()

    if opcion == 'a':
        gestorCliente.actualizarSaldo(gestorMov)
    elif opcion == 'b':
        gestorMov.informarSinMov(gestorCliente, gestorMov, Movimiento.__numero_tar)
    elif opcion == 'c':
        gestorMov.ordenarMov(GestorMov)
    elif opcion == 'x':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")