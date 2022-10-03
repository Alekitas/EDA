class NodoArbol:
    __item=None
    __sigizq=None
    __sigder=None
    def __init__(self,item):
        self.__item=item
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
    
    def getItem(self):
        return self.__item
    
    def setItem(self,item):
        self.__item=item