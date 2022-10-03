from pickle import NONE
from NodoArbol import NodoArbol
class ArbolBinario:
    __raiz=None
    def __init__(self):
        self.__raiz=None
    
    def getraiz(self):
        return self.__raiz
    
    def padre(self,nodoactual,valor):
        band=False
        if nodoactual!=None:
            if nodoactual.getSigIzq() != None and nodoactual.getSigIzq().getItem() == valor:
                return nodoactual

            elif nodoactual.getSigDer() != None and nodoactual.getSigDer().getItem() == valor:
                return nodoactual

                    

    def grado(self,nodoactual):
        grado=0
        if nodoactual != None:
            if nodoactual.getSigIzq() != None and nodoactual.getSigDer() == None:
                grado=1
            elif nodoactual.getSigIzq() == None and nodoactual.getSigDer() != None:
                grado=1
            elif nodoactual.getSigIzq() != None and nodoactual.getSigDer() != None:
                grado=2
        return grado
    
    def maximal(self):
        Nodoactual=NodoArbol()
        max=-1
        while Nodoactual!=None:
            pass

    def minimal(self):
        pass
            

    def insertar(self,nodoactual,valor):
        if nodoactual == None:
            nodoactual=NodoArbol(valor)
            self.__raiz=nodoactual
            print('\nRaiz establecida con el valor: {}'.format(valor))
        else:
            if valor < nodoactual.getItem():
                if nodoactual.getSigIzq() == None:
                    nuevonodo=NodoArbol(valor)
                    nodoactual.setSigIzq(nuevonodo)
                    print('\nHoja nueva del lado izquierdo, valor: {}'.format(valor))
                else:
                    self.insertar(nodoactual.getSigIzq(),valor)
            elif valor > nodoactual.getItem():
                if nodoactual.getSigDer() == None:
                    nuevonodo=NodoArbol(valor)
                    nodoactual.setSigDer(nuevonodo)
                    print('\nHoja nueva del lado derecho, valor: {}'.format(valor))
                else:
                    self.insertar(nodoactual.getSigDer(),valor)
        
    def PreOrden(self,nodoactual):
        if nodoactual != None:
            print(nodoactual.getItem())
            self.InOrden(nodoactual.getSigIzq())
            self.InOrden(nodoactual.getSigDer())

    def InOrden(self,nodoactual): #Muestra de forma Ascendente o Descendentemente segun se recorra del arbol izquierdo o derecho
        if nodoactual != None:
            self.InOrden(nodoactual.getSigIzq())
            print(nodoactual.getItem())
            self.InOrden(nodoactual.getSigDer())        
    
    def PostOrden(self,nodoactual):
        if nodoactual != None:
            self.InOrden(nodoactual.getSigIzq())
            self.InOrden(nodoactual.getSigDer())
            print(nodoactual.getItem())
    
    def Buscar(self,nodoactual,elem):
        if nodoactual!=None:
            if nodoactual.getItem() == elem:
                print('\nElemento existente')
            elif elem < nodoactual.getItem():
                self.Buscar(nodoactual.getSigIzq(),elem)
            elif elem > nodoactual.getItem():
                self.Buscar(nodoactual.getSigDer(),elem)
        else:
            print('\nElemento no existente')

    def suprimir(self,nodoactual,anterior,elem):
        #Si el nodo a suprimir es la raiz y es grado 0
        if nodoactual!=None:
            if nodoactual.getItem()==elem:
                if nodoactual.getSigIzq() == None and nodoactual.getSigDer() == None:
                    print('Nodo Actual es hoja, suprimiendo valor {}...'.format(nodoactual.getItem()))
                    if anterior.getSigDer().getItem() == elem:
                        anterior.setSigDer(None)
                    else:
                        anterior.setSigIzq(None)

            #grado 1 por izquierda    
                elif nodoactual.getSigIzq() != None and nodoactual.getSigDer() == None:
                    valorhijo=nodoactual.getSigIzq().getItem()
                    nodoactual.setItem(valorhijo)
                    nodoactual.setSigIzq(None)

            #grado 1 por derecha
                elif nodoactual.getSigIzq() == None and nodoactual.getSigDer() != None:
                    valorhijo=nodoactual.getSigDer().getItem()
                    nodoactual.setItem(valorhijo)
                    nodoactual.setSigDer(None)
            
            elif elem > nodoactual.getItem():
                self.suprimir(nodoactual.getSigDer(),nodoactual,elem)

            elif elem < nodoactual.getItem():
                self.suprimir(nodoactual.getSigIzq(),nodoactual,elem)