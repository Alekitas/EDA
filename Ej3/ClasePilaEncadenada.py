
from clasecelda import celda
class Encadenada:
    __cant=None
    __tope=None

    def __init__(self,cant=0):
        self.__cant=cant  
        self.__tope=None

    def vacia(self):
        return self.__cant==0

    def insertar(self,x) :
        unacelda=celda()
        unacelda.cargaritem(x)
        unacelda.cargarsig(self.__tope)
        self.__tope=unacelda
        ++self.__cant
        return unacelda.obteneritem()

    def suprimir(self):
       aux=celda()
       x=None
       if (self.vacia()):
            print("Pila vacia")
            return 0
       else:
            aux=self.__tope
            x=self.__tope.obteneritem()
            self.__tope=self.__tope.obtenersig()
            --self.__cant
            del aux
            return x
    def mostrar (self):
        if not (self.vacia()):
            i = self.__cant-1
            tope = self.__tope
            while (i >= 0):
                print(tope.obteneritem())
                tope = tope.obtenersig()
                i -= 1              



           
