# BUSQUEDA EN ARREGLOS NUMPY

def buscaEnArreglo(self, datoUser):
        i = 0
        bandera = False
        while i < self.__cantidad and not bandera:
            if self.__arreglo[i] is not None and self.__arreglo[i].getDatoAComparar() == datoUser:
                bandera = True
            else:
                i += 1
        if bandera:
            return self.__arreglo[i].getQueQuieroEncontrar()
        else:
            return None         
#esta funcion devuelve el valor que se quiere buscar, que debe ser utilizado en otra funcion o modificar si se quiere mostrar

#en caso de necesitar hacer una busqueda en una lista, obtener el dato a comprar, y de ahi recien buscar en el arreglo, se debe hacer dos 
#busquedas entonces, primero en la lista y luego en el arreglo:
#ejemplo: (en el main)
dato1 = int(input("Ingrese el dato asociado a la busqueda: "))          #verificar si es int, float o str
datoAbuscar = gestorA.buscaElDatoEnLista(dato1)
if datoAbuscar is not None:
    gestorB.buscaEnArreglo(datoAbuscar)
else:
    print("Dato no encontrado.")