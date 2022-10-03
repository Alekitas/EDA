from re import I
from NodoLista import NodoLista
class Lista:
    __cabeza=None
    __cantidad=None
    def __init__(self):
        self.__cabeza=None
        self.__cantidad=0
    
    def vacia(self):
        return self.__cabeza == None
    
    def insertar(self,elem,pos):
        if pos >= 0 or pos < self.__cantidad+1:
            unNodo=NodoLista(elem)
            if self.__cabeza == None or pos == 1:
                unNodo.setSiguiente(self.__cabeza)
                self.__cabeza=unNodo
            else:
                aux=self.__cabeza #resguardo la cabeza de la lista
                i=1
                while(i<pos-1): #se itera hasta llegar a la posicion donde deseamos insertar
                    aux=aux.getSiguiente()
                    i+=1
                unNodo.setSiguiente(aux.getSiguiente()) #una vez alcanzada la posicion, establecemos el siguiente del nodo donde insertamos
                aux.setSiguiente(unNodo)
            self.__cantidad+=1 #Como insertamos, aumentamos la cantidad (de nodos) que existen en nuestra lista
        else:
            print('Posicion no valida')
    
    def suprimir(self,pos):
        if not self.vacia():
            if pos > 0 and pos <= self.__cantidad+1:
                aux=self.__cabeza
                i=1
                while(i<pos-1):
                    aux=aux.getSiguiente()
                    i+=1
                nodoelim=aux.getSiguiente()
                aux.setSiguiente(nodoelim.getSiguiente())
                del nodoelim
                self.__cantidad-=1
            else:
                print('Posicion no valida')
        else:
            print('Lista vacia')

    def recorrer(self):
        aux=self.__cabeza
        while(aux!=None):
            print(aux.getElemento())
            aux=aux.getSiguiente()
    
    def primer(self):
        return self.__cabeza.getElemento()
    
    def anterior(self,pos):
        if not self.vacia() and pos!=1:
            aux=self.__cabeza
            i=1
            while(i<pos-1):
                aux=aux.getSiguiente()
                i+=1
            return aux.getElemento()
    
    def getSiguiente(self,pos):
        aux=self.__cabeza
        i=1
        if not self.vacia() and pos < self.__cantidad:
            while(i<pos-1):
                aux=aux.getSiguiente()
                i+=1
            aux.getSiguiente().getElem()
    
    def buscar(self,elem,pos):
        band=False
        aux=self.__cabeza
        
        while(aux!=None) and band == False:
            if(aux.getElemento())==elem:
                band=True 
            aux=aux.getSiguiente()

        if band==True:
            print('Elemento encontrado')
        else:
            print('Elemento no encontrado')
