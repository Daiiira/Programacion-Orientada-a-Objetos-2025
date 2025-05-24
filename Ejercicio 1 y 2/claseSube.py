# Codifique la clase "Tarjeta Sube" utilizando el lenguaje Python, usando módulos.
# Escriba una función test(), que lea desde teclado los datos (los datos los lee dentro de la función), 
# para crear 3 objetos de la clase, verificando el funcionamiento correcto de todos los métodos.
# En otro módulo, hacer el programa principal que invoque a la función test.

# para definir una clase: con los atributos correspondientes siendo atributos privados
class SUBE:
    __numero: int
    __saldo: float

# se inicializan los atributos y con el metodo get, obtenemos el atributo, por ser privado, DENTRO DE LA CLASE
    def __init__(self, numero = 0, saldo = 0):
        self.__numero = numero
        self.__saldo = saldo

    def getNumero(self):
        return self.__numero

    def getSaldo(self):
        return self.__saldo
    
    # seguimos con la definicion de los metodos que involucran a la clase

    # funcion pagar_pasaje: verifica si hay saldo suficiente, si lo hay entonces realiza la operacion e informa el nuevo saldo, 
    # y en caso negativo, devuelve un valor negativo que se deberá chequear para saber si se pudo realizar el pago.
    def pagarPasaje(self, importe):
        if(self.__saldo >= importe):
            self.__saldo -= importe
            print("Saldo: ", self.__saldo)
        else: 
            print("Saldo Insuficiente\n")
    
    # funcion cargar_saldo(importe), debe verificar que el importe sea positivo.
    def cargarSaldo(self, importe):
        if(importe > 0):
            self.__saldo += importe
        else:
            print("El importe debe ser mayor a $0")
    
    # funcion para consultar el saldo de la tarjeta
    def consultaSaldo(self):
        print(f"El saldo de su tarjeta es: $", {self.__saldo})

    # funcion para mostrar los datos, este metodo SIEMPRE VA
    def mostrar(self):
        print(f"Numero de tarjeta: {self.__numero} Saldo: ${self.__saldo}\n")

    