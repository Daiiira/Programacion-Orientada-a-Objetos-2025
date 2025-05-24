import csv
from claseX import claseX

class gestorLista:
    __lista = []

    def __init__(self):
        self.__lista = []

    def getLista(self):
        return self.__lista

    def cargaLista(self):
        archivo = open('archivo.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            var1 = fila[0]
            var2 = fila[1]
            var3 = int(fila[2])                     #si lo que va a leer es un int o float, debo escribirlo antes del input
            var4 = fila[3]
            list = claseX(var1, var2, var3, var4)
            self.__lista.append(list)
        archivo.close()
        print("Lista cargada correctamente.")