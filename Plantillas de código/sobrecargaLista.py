# en la clase del elemento se debe generar la sobrecarga:
def __gt__(self, otro):
        return self.__dato > otro.getDato()

def __lt__(self, otro):
        return self.__dato < otro.getDato()

# luego una funcion realiza la operacion directamente con el operador sobrecargado:
def getDatoMayor(self, dato):
        print("\nDato mayor a: ", dato)
        for clase in self.__lista:
            if clase.getDatoCompara() > dato:
                print(clase)

def getDatoMenor(self, dato):
        print("\nDato menor a: ", dato)
        for clase in self.__lista:
            if clase.getDatoCompara() < dato:
                print(clase)

#__STR__ es el metodo que se ejecuta cuando se imprime la clase
def __str__(self):
        return f"Dato1: {self.__Dato1}, Dato2: {self.__Dato2}, Dato3: {self.__Dato3}"
    