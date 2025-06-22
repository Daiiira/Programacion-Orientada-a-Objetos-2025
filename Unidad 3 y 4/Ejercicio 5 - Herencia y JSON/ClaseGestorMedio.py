from ClaseNodo import Nodo
from ClaseTelevision import Television
from ClaseRadio import Radio
from ClasePrograma import Programa
from ClasePrensa import Prensa
from ClaseMedio import Medio
import csv
class GestorMedio:
    __comienzo:None
    __actual:None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual.getSiguiente()
        return dato
    
    def agregar(self,medio):
        nodo=Nodo(medio)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def mostrarMedios(self):
        auxiliar=self.__comienzo
        while auxiliar != None:
            auxiliar.getDato().mostrarDatos()
            auxiliar=auxiliar.getSiguiente()
                
    def cargar(self):
            with open("C:/Users/gonza/Documents/Facultad/Python/Unidad3/Ejercicio5/medios.csv") as archivo:
                reader=csv.reader(archivo,delimiter=",")
                next(reader)
                for fila in reader:
                    if fila[0] == 'T':
                        nombre=fila[1]
                        canal=int(fila[2])
                        audiencia=int(fila[3])
                        cantp=int(fila[4])
                        unaTele=Television(nombre,canal,audiencia,cantp)
                        with open("C:/Users/gonza/Documents/Facultad/Python/Unidad3/Ejercicio5/programa.csv") as archivo2:
                            reader2=csv.reader(archivo2,delimiter=";")
                            next(reader2)
                            for fila2 in reader2:
                                if fila2[1] == str(canal):
                                    nombre=fila2[2]
                                    horaInicio=fila2[3]
                                    horaFin=fila2[4]
                                    programa=Programa(nombre,horaInicio,horaFin)
                                    unaTele.agregar(programa)
                        self.agregar(unaTele)
                    elif fila[0] == 'R':
                        nombre=fila[1]
                        audiencia=int(fila[3])
                        emisora=fila[5]
                        frecuencia=fila[6]
                        unaRadio=Radio(nombre,audiencia,emisora,frecuencia)
                        with open("C:/Users/gonza/Documents/Facultad/Python/Unidad3/Ejercicio5/programa.csv") as archivo2:
                            reader2=csv.reader(archivo2,delimiter=";")
                            next(reader2)
                            for fila2 in reader2:
                                if fila2[1] == frecuencia:
                                    nombre=fila2[2]
                                    horaInicio=fila2[3]
                                    horaFin=fila2[4]
                                    programa=Programa(nombre,horaInicio,horaFin)
                                    unaRadio.agregar(programa)   
                        self.agregar(unaRadio)
                    elif fila[0] == 'P':
                        nombre=fila[1]
                        audiencia=int(fila[3])
                        tipo=fila[7]
                        periocidad=fila[8]
                        unaPrensa=Prensa(nombre,audiencia,tipo,periocidad)
                        self.agregar(unaPrensa)

    def agregarfinal(self,medio):
        if not isinstance(medio,Medio):
            raise TypeError("\nEl objeto que quiso agregar a la lista no pertenece a la clase MEDIO.")
        nodo=Nodo(medio)
        auxiliar=self.__comienzo
        while auxiliar.getSiguiente() != None:
            anterior=auxiliar
            auxiliar=auxiliar.getSiguiente()
        if anterior != None:
            anterior.setSiguiente(nodo)
    
    def contar(self):
        contDiarios=0
        contRevistas=0
        auxiliar=self.__comienzo
        while auxiliar != None:
            dato=auxiliar.getDato()
            if isinstance(dato,Prensa):
                if dato.getTipo() == "Diario":
                    contDiarios+=1
                else:
                    contRevistas+=1
            auxiliar=auxiliar.getSiguiente()
        print(f"\nLa cantidad de diarios es :{contDiarios}")
        print(f"\nLa cantidad de revistas es :{contRevistas}")

    def buscarprograma(self,nombreP):
        auxiliar=self.__comienzo
        b=False
        while auxiliar != None:
            if isinstance(auxiliar.getDato(),Television):
                for Programa in auxiliar.getDato().getListaP():
                    if Programa.getNombre() == nombreP:
                        b=True
                        print(f"\nPROGRAMA {nombreP}\nNOMBRE DEL CANAL DONDE SE TRANSMITE: {auxiliar.getDato().getNombre()}")
                        print(f"\nHORARIO DE TRANSMISIÓN:\nDESDE:{Programa.getHorainicio()}  HASTA:{Programa.getHorafin()}")
            auxiliar=auxiliar.getSiguiente()
        if b == False:
            print("\nNo se encontró el programa buscado.")

    def buscaremisora(self,nombreE):
        auxiliar=self.__comienzo
        b=False
        while auxiliar != None:
            if isinstance(auxiliar.getDato(),Radio):
                if auxiliar.getDato().getEmisora() == nombreE:
                    b=True
                    auxiliar.getDato().mostrarprograma()
            auxiliar=auxiliar.getSiguiente()
        if b == False:
            print("\nNo se encontró la emisora buscada.")
    
    def crearMedio(self):
        eleccion=-1
        while eleccion != 0:
            eleccion=int(input(("\nELIJA UN MEDIO PARA AGREGAR\n1- TV\n2- RADIO\n3- PRENSA\n0- SALIR\n OPCION:")))
            if eleccion == 1:
                nombre=input("\nIngrese nombre de la television:")
                canal=int(input("\nIngrese canal de la television:"))
                aud=int(input("\nIngrese audiencia:"))
                cantP=int(input("\nIngrese cantidad de programas de la television:"))
                tv=Television(nombre,canal,aud,cantP)
                for i in range(cantP):
                    nombreP=input("\nIngrese nombre del programa:")
                    horai=input("\nIngrese hora de incio del programa:")
                    horaf=input("\nIngrese hora de fin del programa:")
                    programa=Programa(nombreP,horai,horaf)
                    tv.agregar(programa)
                aux=tv
            elif eleccion == 2:
                nombre=input("\nIngrese nombre de la radio:")
                aud=int(input("\nIngrese audiencia:"))
                emisora=input("\nIngrese emisora de la radio:")
                frecuencia=input("\nIngrese frecuencia de la radio:")
                radio=Radio(nombre,aud,emisora,frecuencia)
                cantprogramas=int(input("\nIngrese cantidad de programas de la radio:"))
                for i in range(cantprogramas):
                    nombreP=input("\nIngrese nombre del programa:")
                    horai=input("\nIngrese hora de inicio del programa:")
                    horaf=input("\nIngrese hora de fin del programa:")
                    programa=Programa(nombreP,horai,horaf)
                    radio.agregar(programa)
                aux=radio
            elif eleccion == 3:
                nombre=input("\nIngrese nombre de la prensa:")
                tipo=input("\nIngrese tipo de la prensa:")
                aud=int(input("\nIngrese audiencia:"))
                periodicidad=input("\nIngrese periodicidad de la prensa:")
                prensa=Prensa(nombre,tipo,aud,periodicidad)
                aux=prensa
            else:
                print("\nDebe elegir un numero entre 0 y 3")
        return aux
    
    def insertar(self,indice,medio):
        if indice < 0:
            raise IndexError
        nodo=Nodo(medio)
        if indice == 0:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
        else:
            i=0
            auxiliar=self.__comienzo
            anterior=None
            while auxiliar != None and i<indice:
                anterior=auxiliar
                auxiliar=auxiliar.getSiguiente()
                i+=1
            if i != indice:
                raise IndexError
            anterior.setSiguiente(nodo)
            nodo.setSiguiente(auxiliar)