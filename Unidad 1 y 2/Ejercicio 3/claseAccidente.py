from gestorDepto import gestorDepto

# la clase accidente contiene como atributo un arreglo bidimensional:
class accidente:
    __arreglo = []

    def __init__(self, gestor):
        self.__arreglo = [[0]*12 for i in range(20)]    # 19 filas (0 a 18), 12 columnas (0 a 11)
        self.__gestor = gestor                          # guardamos la referencia al gestorDepto
# genera esta estructura para 12 meses y 19 deptos
#[
# [0, 0]...
# [0, 0]...
# [0, 0]...
#]
    def carga(self, depto_id, mes, cantidad):
        # depto_id es 1–19, mes es 1–12
        fila = depto_id - 1
        columna  = mes - 1
        # validación opcional:
        if 0 <= fila < len(self.__arreglo) and 0 <= columna < 12:
            self.__arreglo[fila][columna] += cantidad
        else:
            print(f"Error: depto {depto_id} o mes {mes} fuera de rango.")    

    def totalAccidentesMes(self, numMes):
        lista = self.__gestor.getLista()
        print(f"\nLos accidentes que hubo en el mes {numMes} son:")
        for i in range(len(lista)):
            cantidad = self.__arreglo[i][numMes - 1]  # numMes - 1 porque los índices van de 0 a 11
            if cantidad > 0:  # <-- este filtro evita mostrar departamentos sin accidentes
                print(f"Nombre del departamento: {lista[i].getNombre()} - Cantidad de accidentes: {cantidad}")

    def mayorCantAccidentes(self, unMes):
        lista = self.__gestor.getLista()
        max_accidentes = -1             # cualquier num real sera mayor a -1 por lo tanto lo guardará y seguirá al siguiente para comparar
        id_max = -1
        for i in range(len(lista)):
            cantidad = self.__arreglo[i][unMes - 1]
            if cantidad > max_accidentes:
                max_accidentes = cantidad
                id_max = i
        if id_max != -1:
            nombre = lista[id_max].getNombre()
            print(f"\nDepartamento con más accidentes en el mes {unMes}:")
            print(f"Nombre: {nombre} - Cantidad de accidentes: {max_accidentes}")
        else:
            print("No se encontraron datos para ese mes.")

    def totAccAnualesDepto(self, depto):
        lista = self.__gestor.getLista()
        # Buscar el índice del departamento que coincide con el nombre
        indice = -1
        for i, departamento in enumerate(lista):
            if departamento.getNombre().lower() == depto.lower():  # compara sin importar mayúsculas
                indice = i
                break
        # Si se encontró el departamento
        if indice != -1:
            total = sum(self.__arreglo[indice])  # suma los 12 meses
            print(f"\nTotal de accidentes en el departamento '{depto}' durante el año: {total}")
        else:
            print(f"Departamento '{depto}' no encontrado.")

    def mostrarTablaCompleta(self):
        lista = self.__gestor.getLista()
        print("Departamento".ljust(20), end="")
        for mes in range(1, 13):
            print(f"{mes:>5}", end="")
        print()
        # Mostrar los datos por departamento
        for i in range(len(lista)):
            print(lista[i].getNombre().ljust(20), end="")
            for mes in range(12):
                print(f"{self.__arreglo[i][mes]:>5}", end="")
            print()
        # Calcular y mostrar la fila TOTAL por mes
        print("TOTAL".ljust(20), end="")
        for mes in range(12):
            total_mes = sum(self.__arreglo[i][mes] for i in range(len(lista)))
            print(f"{total_mes:>5}", end="")
        print()