class NodoCola:
    __elementos=None
    __sig=None
    def __init__(self,elementos=None):
        self.__sig=None
        self.__elementos=elementos

    def setElementos(self,elementos):
        self.__elementos=elementos
    
    def setSig(self,sig):
        self.__sig=sig
    
    def getSig(self):
        return self.__sig
    
    def getElem(self):
        return self.__elementos