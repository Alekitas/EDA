import numpy as np

class ColaSec:
    __max=None
    __cant=0
    __pr=None
    __ul=None
    def __init__(self,max):
        self.__elementos=np.empty(max,dtype=int)
        self.__pr=0
        self.__ul=0
        self.__cant=0
        self.__max=max
    
    def vacia(self):
        return self.__cant == 0
    
    def Insertar(self,obj):
        if self.__cant<self.__max:

            self.__elementos[self.__ul]=obj
            self.__ul=(self.__ul+1)%self.__max
            self.__cant+=1

            return obj
    
    def Suprimir(self):
        obj=None
        if not self.vacia():
            obj=self.__elementos[self.__pr]
            self.__pr=(self.__pr+1)%self.__max
            self.__cant-=1
            return obj
    
    def Recorrer(self):
        if not self.vacia():
            i=0
            while(i<self.__cant):
                print(self.__elementos[i])
                i+=1