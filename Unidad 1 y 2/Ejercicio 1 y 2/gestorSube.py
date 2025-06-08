import claseSube

# el gestor se encarga de actuar como el controlador de la logica del programa
# definimos la clase del controlador
class gestorSube:
    __lista = []

    # inicializamos atributos y definimos metodos propios
    def __init__(self):
        self.__lista = []

    # funcion agregar elementos a la lista
    def agregarDatos(self, tarjeta):
        if type(tarjeta) == claseSube.SUBE:
            self.__lista.append(tarjeta)
    #"Type" is a built-in Python function that returns the exact type of an object. The comparison "type(tarjeta) == TarjetaSube.TarjetaSube" checks if tarjeta is exactly an instance of the class TarjetaSube.TarjetaSube (not a subclass).
    #This is useful when you want to ensure that only objects of a specific class are accepted, avoiding accidental inclusion of other types or subclasses.

    # mostrar los datos en una lista
    def mostrarDatos(self):
        long = len(self.__lista) #saber la longitud de la lista para recorrerla
        for i in range(long):
            print("Tarjeta ingresada número: ", i+1)
            print("Numero: ", self.__lista[i].getNumero(), " Saldo: $", self.__lista[i].getSaldo(), "\n")
        
    # funcion para recorrer la lista de tarjetas con saldo negativo
    def saldoNegativo(self):
        long = len(self.__lista)
        for i in range(long):
            if(self.__lista[i].getSaldo() < 0):
                print("Numero: ", self.__lista[i].getNumero())

    # funcion para obtener el sado de las tarjetas, con una busqueda, itera con una bandera y recorre hasta encontrar el elemento buscado
    def obtenerSaldo(self, numero):
        long = len(self.__lista)
        i = 0
        encontrado = False
        while i < long and encontrado == False:
            if(self.__lista[i].getNumero() == numero):
                encontrado = True
            else:
                i += 1
        if encontrado == True:
            print("El saldo es de: $", self.__lista[i].getSaldo())
        else: 
            print("La tarjeta no está registrada.\n")