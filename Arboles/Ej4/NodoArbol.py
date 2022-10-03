class NodoArbol:
    __caracter=None
    __frecuencia=None
    __sigizq=None
    __sigder=None
    def __init__(self,caracter,frecuencia):
        self.__caracter=caracter
        self.__frecuencia=frecuencia
        self.__sigizq=None
        self.__sigder=None
    
    def getSigIzq(self):
        return self.__sigizq
    
    def getSigDer(self):
        return self.__sigder
    
    def setSigIzq(self,sig):
        self.__sigizq=sig
    
    def setSigDer(self,sig):
        self.__sigder=sig
    
    def getCaracter(self):
        return self.__caracter
    
    def setCaracter(self,caracter):
        self.__caracter=caracter
    
    def getFrecuencia(self):
        return self.__frecuencia
    
    def __gt__(self,other):
        if type(other) == NodoArbol:
            return self.__frecuencia < other.getFrecuencia()
    
    def __eq__(self,other):
        if type(other) == str:
            return self.__caracter == other