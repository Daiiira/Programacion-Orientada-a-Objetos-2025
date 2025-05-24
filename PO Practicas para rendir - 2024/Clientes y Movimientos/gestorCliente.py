import csv
from claseCliente import Cliente

class gestorCliente:
    __lista = []

    def __init__(self):
        self.__lista = []
    
    def getLista(self):
        return self.__lista

    def cargarClientes(self):
        archivo = open('ClientesAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader) 
        for fila in reader:
            nombre = fila[0]
            apellido = fila[1]
            dni = int(fila[2])
            numero_tarjeta = int(fila[3])
            saldo_anterior = float(fila[4])
            cliente = Cliente(nombre, apellido, dni, numero_tarjeta, saldo_anterior)
            self.__lista.append(cliente)    
        archivo.close()
        print("Clientes cargados correctamente.")

    def actualizarSaldo(self, dni, movimientos):
        for cliente in self.__lista:
            if cliente.getDni() == dni:
                tarjeta = cliente.getNumeroTarjeta()
                saldo_actual = cliente.getSaldoAnterior()
                #movimientos_cliente = [mov for mov in movimientos if mov.getNumeroCuenta() == tarjeta]
                print(f"Cliente: {cliente.getNombre()} {cliente.getApellido()}          Número de tarjeta: {cliente.getNumeroTarjeta()}")
                print(f"Saldo anterior: ${saldo_actual}")
                print(f"Movimientos:")
                print(f"{'Fecha:':<13}{'Descripción:':<20}{'Importe:':>13}{'Tipo de mov:':>15}")
                i = 0
                while i < movimientos.getCantidad():
                    mov = movimientos.getMovimiento(i)
                    if mov.getNumeroCuenta() == tarjeta:
                        if mov.getTipoMovimiento() == "C":
                            saldo_actual -= mov.getImporte()
                        elif mov.getTipoMovimiento() == "P":
                            saldo_actual += mov.getImporte()
                        print(f"{mov.getFecha():<13}{mov.getDescripcion():<20}${mov.getImporte():>12.2f}{mov.getTipoMovimiento():>15}")
                    i += 1
                print(f"Saldo actualizado: ${saldo_actual}")
                return
        print("Cliente no encontrado.")