import numpy as np
class Pila:
    __cant=None
    __tope1=None
    __tope2=None
    __arreglo=None

    def __init__(self,cant=0):
        self.__cant=cant
        self.__tope1=-1
        self.__tope2=int(cant)-1
        self.__arreglo=np.empty(int(cant),dtype=int)

    def vacia(self):
        return self.__tope1 == -1
    
    def llena(self):
        return self.__tope1+1 == self.__tope2
    
    def llena2(self):
        return self.__tope2 == self.__tope1

    def vacia2(self):
        return (self.__tope2 == len(self.__arreglo)-1)
    
    def suprimir1(self):
        valor=None
        if self.vacia() == True:
            print('Pila vacia')
        else:
            valor=self.__arreglo[self.__tope1-1]
            self.__tope1-=1
        return valor
    
    def Suprimir2(self):
        valor=None
        if self.vacia2()==True:
            print('Pila 2 vacia')
        else:
            valor=self.__arreglo[self.__tope2+1]
            self.__tope2+=1
        return valor
    
    def insertar1(self,obj):
        if self.__tope1 <= self.__tope2 and self.__tope1 < len(self.__arreglo):
            self.__tope1+=1
            self.__arreglo[self.__tope1]=obj
        else:
            print('La pila 1 no puede crecer mas')

    def insertar2(self,obj):
        if self.__tope1 <= self.__tope2 and self.__tope2 >=0:
            self.__arreglo[self.__tope2]=obj
            self.__tope2-=1
        else:
            print('La pila 2 no puede crecer mas')

    def Mostrar1(self):
        if not self.vacia():
            i=self.__tope1
            while(i>=0):
                print('{}'.format(self.suprimir1()))
                i+=1
        else:
            print('Pila Vacia')
    
    def Mostrar2(self):
        if not self.vacia2():
            i=self.__tope2
            while(i<=self.__cant):
                print('{}'.format(self.Suprimir2()))
        else:
            print('Pila Vacia')