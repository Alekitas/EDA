from Arbol import ArbolBinario
from NodoArbol import NodoArbol

def test():
    unArbol=ArbolBinario()
    unArbol.insertar(unArbol.getraiz(),6)
    unArbol.insertar(unArbol.getraiz(),4)
    unArbol.insertar(unArbol.getraiz(),2)
    unArbol.insertar(unArbol.getraiz(),5)
    unArbol.insertar(unArbol.getraiz(),8)
    unArbol.insertar(unArbol.getraiz(),10)
    

    '''unArbol.InOrden(unArbol.getraiz())
    unArbol.Buscar(unArbol.getraiz(),11)
    print('------------------------------')
    unArbol.suprimir(unArbol.getraiz(),unArbol.getraiz(),6)
    unArbol.InOrden(unArbol.getraiz())'''

    unArbol.minimal(unArbol.getraiz())

if __name__ == '__main__':
    test()