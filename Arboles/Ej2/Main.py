from Arbol import ArbolBinario
from NodoArbol import NodoArbol

def test():
    nivel=0
    unArbol=ArbolBinario()
    unArbol.insertar(unArbol.getraiz(),10)
    unArbol.insertar(unArbol.getraiz(),3)
    unArbol.insertar(unArbol.getraiz(),12)
    unArbol.insertar(unArbol.getraiz(),2)
    unArbol.insertar(unArbol.getraiz(),5)
    unArbol.insertar(unArbol.getraiz(),7)
    unArbol.insertar(unArbol.getraiz(),11)
    unArbol.insertar(unArbol.getraiz(),15)
    unArbol.insertar(unArbol.getraiz(),14)
    

    unArbol.InOrden(unArbol.getraiz())
    print('------------------------------')
    '''unArbol.suprimir(unArbol.getraiz(),unArbol.getraiz(),12)'''
    unArbol.InOrden(unArbol.getraiz())


    '''unArbol.frontera(unArbol.getraiz())
    print('------------------------------')
    unArbol.hermano(unArbol.getraiz(),unArbol.getraiz(),11)
    print('------------------------------')
    cantnodos=unArbol.cantNodos(unArbol.getraiz())
    print('\nCantidad de nodos del arbol: {}'.format(cantnodos))
    unArbol.nivel(unArbol.getraiz(),7)'''
    
    altura=unArbol.altura(unArbol.getraiz())
    print('\nAltura del Arbol: {}'.format(altura))

    unArbol.sucesores(3)
    
if __name__ == '__main__':
    test()