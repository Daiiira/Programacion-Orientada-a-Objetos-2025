# Guevara Daira Martina - DNI 45885184 - Registro E010-311

class visita:
    __fecha = str
    __dniPaciente = int
    __zonaVisita = str
    __dniMedico = int
    __diagnostico = str

    def __init__(self, fecha, dniPaciente, zonaVisita, dniMedico, diagnostico):
        self.__fecha = fecha
        self.__dniPaciente = dniPaciente
        self.__zonaVisita = zonaVisita
        self.__dniMedico = dniMedico
        self.__diagnostico = diagnostico

    def getFecha(self):
        return self.__fecha
    def getDniPaciente(self):
        return self.__dniPaciente
    def getZonaVisita(self):
        return self.__zonaVisita
    def getDniMedico(self):
        return self.__dniMedico
    def getDiagnostico(self):
        return self.__diagnostico
    
    def __str__(self):
        return f"Fecha: {self.__fecha} - DNI Paciente: {self.__dniPaciente} - Zona: {self.__zonaVisita} - DNI Medico: {self.__dniMedico} - Diagnostico: {self.__diagnostico}"