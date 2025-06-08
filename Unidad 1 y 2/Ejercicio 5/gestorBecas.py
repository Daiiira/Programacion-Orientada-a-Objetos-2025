import csv
from claseBeca import beca

class gestorBecas:
    __lista = []

    def __init__(self):
        self.__lista = []

    def cargarBecas(self):
        archivo = open('Becas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            idBeca = int(fila[0])
            tipoBeca = fila[1]
            montoBeca = float(fila[2])
            bec = beca(idBeca, tipoBeca, montoBeca)
            self.__lista.append(bec)
        archivo.close()
        print("Becas cargadas correctamente.")

    def getLista(self):
        return self.__lista
    
    def muestraListaTotal(self, tipoBeca, GBen):
        print(f"\nLista de beneficiarios para la Beca tipo '{tipoBeca}':")
        beca_encontrada = None
        for beca in self.__lista:
            if beca.getTipoBeca().lower() == tipoBeca.lower():
                beca_encontrada = beca
                break

        if beca_encontrada is None:
            print("No se encontró una beca con ese tipo.")
            return

        total = 0
        beneficiarios = [b for b in GBen.getLista() if b.getIdBecaAsig() == beca_encontrada.getIdBeca()] #Filtra la lista de beneficiarios y se queda solo con los que tienen asignada la beca seleccionada.
        if not beneficiarios:
            print("No hay beneficiarios para esta beca.")
        else:
            for beneficiario in beneficiarios:
                print(beneficiario)
                total += beca_encontrada.getMontoBeca()
            print(f"Total a abonar: ${total}\n")