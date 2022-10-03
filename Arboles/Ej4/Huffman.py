import string
from NodoArbol import NodoArbol

class ArbolHuffman:
    __raiz=None
    
    def __init__(self):
        lista=[]
        archivo=open('huffman.txt','r')
        texto=""
        for linea in archivo:
            texto+=linea
        archivo.close()

        texto = texto.translate({ord(c): None for c in string.whitespace}).lower()

        for i in range(len(texto)):
            if texto[i] not in lista:
                unNodo=NodoArbol(texto[i],texto.count(texto[i]))
                lista.append(unNodo)
        lista.sort()

        while len(lista)>=2:
            NodoNuevo=NodoArbol(lista[0].getCaracter()+lista[1].getCaracter(),lista[0].getFrecuencia()+lista[1].getFrecuencia())
            NodoNuevo.setSigIzq(lista[0])
            NodoNuevo.setSigDer(lista[1])
            lista.pop(0)
            lista.pop(0)
            lista.append(NodoNuevo)
            lista.sort()
        
        self.__raiz=lista[0]

    def InOrden(self,nodoactual):
        if nodoactual!=None:
            self.InOrden(nodoactual.getSigIzq())
            print(nodoactual.getCaracter())
            self.InOrden(nodoactual.getSigDer())
    
    def getraiz(self):
        return self.__raiz
