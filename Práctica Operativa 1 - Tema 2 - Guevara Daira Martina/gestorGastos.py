import csv
from claseGasto import Gasto

class gestorGas:
    __lista = []

    def __init__(self):
        self.__lista = []

    def getLista(self):
        return self.__lista
    
    def cargaGas(self):
        archivo = open("gastosAbril2025.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader) 
        for fila in reader:
            patenteGas = fila[0]
            fecha = fila[1]
            importe = fila[2]
            descripcion = fila[3]
            self.__lista.append(Gasto(patenteGas, fecha, importe, descripcion))
        archivo.close()
            
    def totalGastosDia(self, fecha):
        total = 0
        print("\nGastos del día", fecha)
        print("Patente       Importe       Descripción")
        for gasto in self.__lista:
            if gasto.getFecha() == fecha:
                print(f"{gasto.getPatente():<13}{gasto.getImporte():<13}{gasto.getDescripcion()}")
                total += float(gasto.getImporte())
        print(f"\nTotal general a pagar: {total}")
    
    def totalGastosMov(self, patente):
        total = 0
        for gasto in self.__lista:
            if gasto.getPatente().lower() == patente.lower():
                total += float(gasto.getImporte())
        return total
    
    def ordenar(self):
        self.__lista = sorted(self.__lista)
    
    def gastosPorFechaOrdenados(self, fecha, movs):
        self.ordenar()
        resumen = {}                # crea el "diccionario" que usara para almacenar los gastos totales
        for gasto in self.__lista:
            if gasto.getFecha() == fecha:           #segun la fecha indicada por el usuario, que haga match con una fecha del arreglo
                pat = gasto.getPatente()
                if pat not in resumen:
                    resumen[pat] = gasto.getImporte()
                else:
                    resumen[pat] += gasto.getImporte()

        if len(resumen) == 0:
            print(f"No se registraron gastos el día {fecha}.")
            return

        print(f"\nGastos por movilidad el día {fecha}:")
        print("Patente     Marca         Modelo        Total Gasto")
        for pat in sorted(resumen):  # orden por patente
            movilidad = movs.buscarMovPorPatente(pat)
            if movilidad:
                print(f"{pat:<12}{movilidad.getMarca():<14}{movilidad.getModelo():<14}{resumen[pat]}")
            else:
                print(f"{pat:<12}{'Desconocido':<14}{'Desconocido':<14}{resumen[pat]}")