import csv
from claseBeneficiario import beneficiario

class gestorBeneficiarios:
    __lista = []

    def __init__(self):
        self.__lista = []
    
    def cargarBeneficiarios(self):
        archivo = open('Beneficiarios.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            dni = int(fila[0])
            nombre = fila[1]
            apellido = fila[2]
            carrera = fila[3]
            facultad = fila[4]
            año = int(fila[5])
            promedio = float(fila[6])
            idBecaAsig = int(fila[7])
            ben = beneficiario(dni, nombre, apellido, carrera, facultad, año, promedio, idBecaAsig)
            self.__lista.append(ben) 
        archivo.close()
        print("Beneficiarios cargados correctamente.") 
    
    def getLista(self):
        return self.__lista
    
    def beneficiariosConMasDeUnaBeca(self, dni):
        cont = 0
        nom = ""
        ape = ""
        for beneficiario in self.__lista:
            if beneficiario.getDni() == dni:
                cont += 1
                nom = beneficiario.getNombre()
                ape = beneficiario.getApellido()
        if cont > 1:
            print(f"Beneficiario con más de una beca: {nom} {ape}")
        elif cont == 1:
            print("El beneficiario tiene sólo una beca.")
        else:
            print("El beneficiario no tiene becas asignadas.")
    
    def listaOrdenada(self):
        self.__lista = sorted(self.__lista)
        print("Beneficiarios ordenados correctamente.\n")
        print("Lista de beneficiarios ordenada por facultad:")
        for beneficiario in self.__lista:
            print(beneficiario)

    def estudiantesSinBeca(self):
        print(f"Estudiantes sin beca 'Ayuda Económica' con promedio mayor a 8:")
        print("Nombre y Apellido:           Promedio:")
        for beneficiario in self.__lista:
            if beneficiario.getIdBecaAsig() != 4:
                if beneficiario.getPromedio() > 8:
                    print(f"{beneficiario.getNombre()} {beneficiario.getApellido():<13} {beneficiario.getPromedio():>13}")