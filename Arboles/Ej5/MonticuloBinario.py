import numpy as np
import math
class Monticulo:
    __arreglo=None
    __dimension=None
    def __init__(self,dimension):
        self.__arreglo=np.empty(dimension,dtype=int)
        self.__arreglo[0]=0
        self.__dimension=dimension
    
    def insertar(self,item):
        self.__arreglo[self.__arreglo[0]+1]=item
        padre=math.floor(self.__arreglo[0]+1/2)
        actual=self.__arreglo[0]+1

        while padre != 0 and self.__arreglo[padre] > self.__arreglo[actual]:
            aux=self.__arreglo[actual]
            self.__arreglo[actual]=self.__arreglo[padre]
            self.__arreglo[padre]=aux

            actual=padre
            padre=math.floor(actual/2)
        
        self.__arreglo[0]+=1
    
    def mostrar(self):
        for i in range(1,self.__arreglo[0]+1):
            print(self.__arreglo[i])
