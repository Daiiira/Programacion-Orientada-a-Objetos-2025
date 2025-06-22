def Menu(GestorM):
    opcion=-1
    while opcion != 0:   
        opcion=int(input("\n1-INSERTAR MEDIO\n2-AGREGAR MEDIOS AL FINAL DE LA LISTA\n3-LISTAR MEDIOS\n4-BUSCAR PROGRAMA DE TV\n5-BUSCAR EMISORA DE RADIO\n6-CONTAR REVISTAS Y DIARIOS\n0-Salir\nINGRESE OPCION:"))
        if opcion == 1:
            indice=int(input("\nIngrese posicion donde desea agregar el medio:"))
            medio=GestorM.crearMedio()
            try:
                GestorM.insertar(indice-1,medio)
            except IndexError:
                print("\nError al insertar posición ingresada no es válida.")
        elif opcion == 2:
            medio=GestorM.crearmedio()
            try:
                GestorM.agregarfinal(medio)
                print("\nMedio agregado con éxito.")
            except TypeError:
                print("\nEl objeto que quiso agregar no pertenece a la clase Medio.") 
        elif opcion == 3:
            GestorM.mostrarMedios()
        elif opcion == 4:
            nombreP=input("\nIngrese nombre del programa que desea buscar:")
            GestorM.buscarprograma(nombreP)
        elif opcion == 5:
            nombreE=input("\nIngrese nombre de la emisora que desea buscar:")
            GestorM.buscaremisora(nombreE)
        elif opcion == 6:
            GestorM.contar()
        elif opcion == 0:
            print("\nSaliendo...")
        else:
            print("\nDebe elegir un numero entre 0 y 6.")
