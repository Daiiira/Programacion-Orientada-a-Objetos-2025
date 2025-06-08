# Guevara Daira Martina - DNI 45885184 - Registro E010-311
import csv
from claseVisita import visita

class gestorVisitas:
    __lista = []

    def __init__(self):
        self.__lista = []

    def getLista(self):
        return self.__lista

    def cargaVisitas(self):
        archivo = open('visitas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            fecha = fila[0]
            dniPac = int(fila[1])
            zona = fila[2]
            dniMed = int(fila[3])                  
            diag = fila[4]
            list = visita(fecha, dniPac, zona, dniMed, diag)
            self.__lista.append(list)
        archivo.close()
        print("Archivo Visitas cargado correctamente.")

    def visitasTotal(self, dni):
        cont = 0
        for i in range(len(self.__lista)):
            if dni == self.__lista[i].getDniMedico():
                cont += 1
        return cont
    
    def visitasPorMedico(self, dni):
        cont = 0
        i = 0
        while i < len(self.__lista):
            if dni == self.__lista[i].getDniMedico():
                print(f"Fecha: {self.__lista[i].getFecha()} - Zona: {self.__lista[i].getZonaVisita()} - Diagnostico: {self.__lista[i].getDiagnostico()}")
                cont += 1
            i += 1
        if cont == 0:
            print(f"No se encontró registro con el DNI ingresado.")
        else:
            print(f"\nTotal de visitas realizadas por el médico con DNI {dni}: {cont}")

    def visitasPorZona(self, zona, med):
        cont = 0
        nombreMedico = med.obtenerNombreMedico(zona)
        for i in range(len(self.__lista)):
            if zona.lower() == self.__lista[i].getZonaVisita().lower():
                print(f"Fecha: {self.__lista[i].getFecha()} - DNI Paciente: {self.__lista[i].getDniPaciente()} - Nombre del Médico: {nombreMedico} - Diagnostico: {self.__lista[i].getDiagnostico()}")
                cont += 1
        if cont == 0:
            print(f"No se encontró registro de la zona ingresada.")
        else:
            print(f"Total de visitas realizadas en la zona {zona}: {cont}")