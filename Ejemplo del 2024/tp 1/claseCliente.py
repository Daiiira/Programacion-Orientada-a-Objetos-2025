import csv
from claseMov import Movimiento

class Cliente:
  def __init__(self, nom, ape, dni, num_tarjeta, saldo_anterior):  #creacion de la clase ya con sus atributos
    self.nom = nom
    self.ape = ape
    self.dni = dni                         
    self.num_tarjeta = num_tarjeta
    self.saldo_anterior = saldo_anterior

class gestorCliente():
  def __init__(self):
    lista = []
    
  def cargarCliente(self):
    with open("poo u2/Trabajo Practico 1 POO/ClientesAbril2024.csv", newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        Cliente = Cliente(fila)
        self.lista.append(Cliente)
    print("\n")
    
  def mostrar(self):
    for Cliente in self.lista:
      print(Cliente)

  def actualizarSaldo(self, gestorMov):
      dni = input("Ingrese DNI: ")
      for Cliente in self.lista:
        if Cliente.dni == dni:
          print(f"Cliente: {Cliente.nom, Cliente.ape} \n")
          print(f"Número de Tarjeta: {Movimiento.numero_tar} \n")
          print(f"Cliente: {Cliente.saldo_anterior} \n")
          print("Movimientos: \n")
          print(f"Fecha:    Descripción:    Importe:    Tipo de movimiento: \n")
          Cliente.saldo = gestorMov.actSaldo(gestorCliente, gestorMov, dni) 
          print(f"Saldo actualizado: {Cliente.saldo} \n")

