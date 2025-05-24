#BUSCAR EN UNA LISTA DE OBJETOS

def buscaEnLista(self, datoUser):
        acum = 0                                        #por si necesito mostrar un total de algo
        print(f"\nAcá se muestran los datos a buscar según el dato ingresado por el User {datoUser}:")
        for clase in self.__lista:
            if clase.getDatoAComparar() == datoUser:
                VAR1 = clase.getVAR1()                  #encuentro las variables que quiero mostrar
                VAR2 = clase.getVAR2()
                VAR3 = clase.getVAR3()
                #[...]
                print(f"Los datos que buscaba son: {VAR1}, {VAR2}, {VAR3}")
                acum += varX                            #acumulo lo que necesite    
        print(f"\nTotal de Xcosa que me pidan {acum}")