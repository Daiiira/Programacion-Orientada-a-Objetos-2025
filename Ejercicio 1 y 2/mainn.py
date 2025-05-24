from claseSube import SUBE
from gestorSube import gestorSube

# funcion test para efectuar que todas las funciones esten ok
def test():
    tarjeta = SUBE(1234, 2000)
    tarjeta.mostrar()
    tarjeta.cargarSaldo(1000)
    tarjeta.mostrar()
    tarjeta.pagarPasaje(750)
    tarjeta.pagarPasaje(2300)
    tarjeta.cargarSaldo(-1000)
    print()

# creamos el inicio del programa: el main
if __name__ == '__main__':
    #test()

    control = gestorSube()
    for i in range (3):
        numero = int(input("Ingrese el numero de la tarjeta: ")) # solicitamos al usuario que ingrese los datos por teclado
        saldo = float(input("Ingrese el saldo de la misma: $"))
        print("\n")
        tarjeta = SUBE(numero, saldo)
        control.agregarDatos(tarjeta)
    control.mostrarDatos()
    control.saldoNegativo()
    control.obtenerSaldo(1234)
