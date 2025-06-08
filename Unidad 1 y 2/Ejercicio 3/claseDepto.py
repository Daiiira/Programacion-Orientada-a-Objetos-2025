class departamento:
    __ID: int
    __nombre: str

    def __init__(self, ID, nombre):
        self.__ID = ID
        self.__nombre = nombre

    def getID(self):
        return self.__ID
    def getNombre(self):
        return self.__nombre
    
    # MOSTRAR funcionalidad que siempre va
    def mostrarDatos(self):
        print(f"Departamento: {self.__nombre} - ID: {self.__ID}")
        