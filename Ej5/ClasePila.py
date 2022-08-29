import numpy as np
class Pila:
    __cant=0
    __tope=-1
    def __init__(self,cant):
        self.__arre=np.empty(cant,dtype=int)
        self.__tope=-1
        self.__cant=cant
    
    def vacia(self):
        return self.__tope == -1
    
    def llena(self):
        return self.__tope == self.__cant
    
    def Ultimo(self):
        return self.__arre[self.__tope]
    
    def Insertar(self,obj):
        if (self.__tope<self.__cant):
            self.__tope+=1
            self.__arre[self.__tope]=obj
            return obj
        else:
            print('Pila Vacia')
    
    def Suprimir(self):
        obj=None
        if not self.vacia():
            obj=self.__arre[self.__tope]
            self.__tope-=1
            return obj
        else:
            print('Pila vacia')
        
    def Mostrar(self):
        if not self.vacia():
            i=self.__tope
            while(i>=0):
                print(self.__arre[i])
                i-=1