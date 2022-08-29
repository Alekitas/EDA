class celda:
    __item=None
    __sig=None

    def obteneritem(self):
        return self.__item

    def cargaritem(self,x):
        self.__item=x

    def cargarsig(self,xtope):
        self.__sig=xtope

    def obtenersig(self):
        return(self.__sig)
