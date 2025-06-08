class facultad:
    __codFacu = int
    __nomFacu = str
    __direccion = str
    __localidad = str
    __telefono = int

    def __init__(self, codFacu, nomFacu, direccion, localidad, telefono):
        self.__codFacu = codFacu
        self.__nomFacu = nomFacu
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono

    def getCodFacu(self):
        return self.__codFacu
    def getNomFacu(self):
        return self.__nomFacu
    def getDireccion(self):
        return self.__direccion
    def getLocalidad(self):
        return self.__localidad
    def getTelefono(self):
        return self.__telefono
    
    def __str__(self):
        return (f"Código: {self.__codFacu}, Nombre: {self.__nomFacu}, "
                f"Dirección: {self.__direccion}, Localidad: {self.__localidad}, "
                f"Teléfono: {self.__telefono}")