from operator import itemgetter
from NodoArbol import NodoArbol

class ArbolBinario:
    __raiz=None
    def __init__(self):
        self.__raiz=None
    
    def getraiz(self):
        return self.__raiz
    
    def padre(self,nodoactual,valor):
        if nodoactual!=None:
            if nodoactual.getSigIzq() != None and nodoactual.getSigIzq().getItem() == valor:
                print('\nPadre del nodo {}: {}'.format(valor,nodoactual.getItem()))
                return nodoactual

            elif nodoactual.getSigDer() != None and nodoactual.getSigDer().getItem() == valor:
                print('\nPadre del nodo {}: {}'.format(valor,nodoactual.getItem()))
                return nodoactual
            
            elif nodoactual.getItem() > valor:
                return self.padre(nodoactual.getSigIzq(),valor)
            
            else:
                return self.padre(nodoactual.getSigDer(),valor)

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
    
    def maximal(self,nodoactual):
        while nodoactual.getSigIzq()!=None:
            nodoactual=nodoactual.getSigIzq()
        return nodoactual         

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
                print('\nElemento existente, retornando nodo...')
                return nodoactual
            elif elem < nodoactual.getItem():
                return self.Buscar(nodoactual.getSigIzq(),elem)
            elif elem > nodoactual.getItem():
                return self.Buscar(nodoactual.getSigDer(),elem)
        else:
            return None
            print('\nElemento no existente')

    def suprimir(self,nodoactual,anterior,item):
        #Si el nodo a suprimir es la raiz y es grado 0
        if nodoactual!=None:
            if nodoactual.getItem()==item:
                #Si es Hoja suprime
                if nodoactual.getSigIzq() == None and nodoactual.getSigDer() == None:
                    print('Nodo Actual es hoja, suprimiendo valor {}...'.format(nodoactual.getItem()))
                    if anterior.getSigDer().getItem() == item:
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

            #grado 2 el que va a reemplazar al nodo a suprimir será o el mayor de los menores (arbol izq) o el menor de los mayores (arbol der)   
                elif nodoactual.getSigIzq() != None and nodoactual.getSigDer() != None:
                    valorhijo=self.maximal(nodoactual.getSigDer())
                    nodoactual.setItem(valorhijo)

            #Si el nodo ingresado no es = al nodo actual, vuelve a llamar segun el valor (si el valor es mayor a la raiz por izq, sino irá por der)
            elif item > nodoactual.getItem():
                self.suprimir(nodoactual.getSigDer(),nodoactual,item)

            elif item < nodoactual.getItem():
                self.suprimir(nodoactual.getSigIzq(),nodoactual,item)
        
        print('\nArbol vacio')
    
    #Muestra los nodos sin hijos (Hojas)
    def frontera(self,nodoactual):
        if nodoactual!=None:
            if self.grado(nodoactual) == 0:
                print(nodoactual.getItem())
            self.frontera(nodoactual.getSigIzq())
            self.frontera(nodoactual.getSigDer())

    #segun un nodo, nos da el hermano (Nodo del mismo nivel con el mismo padre)
    def hermano(self,nodoactual,anterior,item):
        if nodoactual!=None: 
            nodoencontrado=self.Buscar(self.__raiz,item)
            padre=self.padre(self.__raiz,nodoencontrado.getItem())
            if nodoencontrado!= None:
                if self.grado(padre) == 2:
                
                    if padre.getSigIzq() != None and padre.getSigIzq().getItem() != item:
                        print('\nHermano del nodo {}: {}'.format(nodoencontrado.getItem(),padre.getSigIzq().getItem()))

                    elif padre.getSigDer() != None and padre.getSigDer().getItem() != item:
                        print('\nHermano del nodo {}: {}'.format(nodoencontrado.getItem(),padre.getSigDer().getItem()))

                else:
                    print('\nEl nodo {} no tiene 2 hijos, por lo tanto no se puede hallar el hermano del nodo ingresado.'.format(nodoactual.getItem()))
            else:
                print('\nNodo no encontrado')
        else:
            print('\nArbol vacio')
    
    def cantNodos(self,nodoactual):
        if self.__raiz==None:
            return 0
        else:
            if nodoactual==None:
                return 0
            else:
                return 1 + self.cantNodos(nodoactual.getSigIzq()) + self.cantNodos(nodoactual.getSigDer())
    
    def nivel(self,nodoactual,valor):
        nivel=0
        while nodoactual!=None:
            if nodoactual.getItem() == valor:
                nodoactual=None
            elif valor < nodoactual.getItem():
                nodoactual=nodoactual.getSigIzq()
            elif valor > nodoactual.getItem():
                nodoactual=nodoactual.getSigDer()
            nivel+=1
        print('\nNivel del nodo {}: {}'.format(valor,nivel))
        return nivel
    
    def altura(self,nodoactual,max=-1):
        if nodoactual!=None:
            nivel=self.nivel(self.__raiz,nodoactual.getItem())
            if max<nivel:
                max=nivel
            max=self.altura(nodoactual.getSigIzq(),max)
            max=self.altura(nodoactual.getSigDer(),max)
        return max
    
    def sucesores(self,item):
        nodoencontrado=self.Buscar(self.__raiz,item)
        if nodoencontrado!=None:
            self.InOrden(nodoencontrado.getSigIzq())
            self.InOrden(nodoencontrado.getSigDer())