class clase:
    __VAR_Ins1 = str        #asigna TIPO DE DATO
    __VAR_Ins2 = str
    __VAR_Cls1 = 35         #asigna VALOR POR DEFECTO

    def __init__(self, VAR_Ins1, VAR_Ins2):
        self.__VAR_Ins1 = VAR_Ins1
        self.__VAR_Ins2 = VAR_Ins2

    def getVAR_Ins1(self):
        return self.__VAR_Ins1
    def getVAR_Ins2(self):
        return self.__VAR_Ins2
    
    @classmethod
    def getVAR_Cls1(cls):
        return cls.__VAR_Cls1
    
    def __str__(self):
        return f'VAR1: {self.__VAR_Ins1}, VAR2: {self.__VAR_Ins2}, VAR_CLS1: {self.__VAR_Cls1}'