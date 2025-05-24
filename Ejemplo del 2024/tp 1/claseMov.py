import numpy as np                                                       
import csv
from claseCliente import Cliente

class Movimiento:
  def __init__(self, numero_tar, fecha, descripcion, tipo_mov, importe):  #creacion de la clase ya con sus atributos
    self.numero_tar = numero_tar
    self.fecha = fecha
    self.descripcion = descripcion                         
    self.tipo_mov = tipo_mov
    self.importe = importe

class gestorMov():
  def __init__(self):
    self.__lista = np.array([], dtype='object')
    
  def cargarMov(self):
    with open("poo u2/Trabajo Practico 1 POO/MovimientosAbril2024.csv",newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        movimiento = movimiento(fila)
        self.__lista = np.append(self.__lista, movimiento)

  def mostrar(self):
    for movimiento in self.__lista:
      print(movimiento)

  def ordenarMov(self):
    self.movimiento = np.sort(self.movimiento, order='numero_tar')

  def actSaldo():
    for movimiento in Movimiento:
      if Cliente.__num_tarjeta == movimiento.numero_tar:
        saldo_actualizado: Cliente.__saldo_anterior
        print(f"{movimiento.fecha}      {movimiento.descripcion}        {movimiento.importe:.2f}        {movimiento.tipo_mov} \n")
        if movimiento.tipo_mov == 'C':
            saldo_actualizado -= movimiento.importe
        elif movimiento.tipo_mov == 'P':
            saldo_actualizado += movimiento.importe
        return saldo_actualizado
      print("No se encontró un cliente con ese DNI")

  def informarSinMov(gestorClientes, gestorMov, numero_tar):
      sin_movimientos = True
      print("\n Clientes sin movimientos en el mes: \n")
      for cliente in gestorClientes.clientes:
          if cliente.num_tarjeta == numero_tar:
              for movimiento in gestorMov.movimientos:
                  if movimiento.num_tarjeta == numero_tar:
                      sin_movimientos = False
                      break
              if sin_movimientos:
                  print(f"\n Apellido y nombre del cliente: {Cliente.ape} {Cliente.nom} \n")
      if sin_movimientos == False:
          print("El cliente ingresado tuvo movimientos en el mes de Abril. \n")
