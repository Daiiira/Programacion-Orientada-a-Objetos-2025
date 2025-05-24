#acá está cuando piden esto:
# Patente: xx-xxx-xx Tipo: XXXXXXXXXX Capacidad de Carga:xxxx
#Importe Mensual de Patente: xxxxxxx Marca: xxxxxxxxxxx Modelo: xxxxxxx
#Gastos
#Fecha Importe Descripción
#xx/xx/xxxx xxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xx/xx/xxxx xxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xx/xx/xxxx xxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Total de Gastos (incluye Patente): xxxxxxxx

print(f"Patente: {mov.getPatenteMov()} Tipo: {mov.getTipoMov()} Capacidad de Carga: {mov.getCapacidadMov()}")
print(f"Importe Mensual de Patente: {mov.getImporteMov()} Marca: {mov.getMarca()} Modelo: {mov.getModelo()}")
print("\nGastos\nFecha           Importe       Descripción")
print(f"Dato1: {clase.getDato1()}          Dato2: {clase.getDato2()}")

print(f"Lista de Datos:")                                                       #esto va fuera del for, se imrpime una sola vez
print(f"{'DatoA:':<13}{'DatoB:':<20}{'DatoC:':>13}{'DatoD:':>15}")              #esto va fuera del for, se imrpime una sola vez
print(f"{DatoA:<12}{clase.getDatoB():<14}{clase.getDatoC():<14}{datoD}")        #esto va dentro del for, se imprime varias veces
print(f"DatoXTotal: ${datoX}")                                                  #si se necesita mostrar el total, se imprime una sola vez fuera del for