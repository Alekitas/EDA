from NodoCola import NodoCola

class ColaEn:
    __cabeza=None
    __ultimo=None
    def __init__(self):
       self.__cabeza=None
       self.__ultimo=self.__cabeza

    def vacia(self):
        return self.__cabeza == None
    
    def insertar(self,elemento):
        unNodo=NodoCola(elemento)
        if self.vacia():
            self.__cabeza=unNodo
            self.__ultimo=unNodo
        else:
            self.__ultimo.setSig(unNodo)
            self.__ultimo=unNodo
    
    def suprimir(self):
        valor=None
        if self.vacia():
            print('Cola vacia')
        else:
            valor=self.__cabeza.getElem()
            self.__cabeza=self.__cabeza.getSig()
        return valor
    
    def recorrer(self):
        aux=self.__cabeza
        i=1
        while(aux!=None):
            print(str(i) + ': ' + str(aux.getElem()))
            aux=aux.getSig()
            i+=1