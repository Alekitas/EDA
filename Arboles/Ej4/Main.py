from NodoArbol import NodoArbol
from Huffman import ArbolHuffman

def test():
    unArbolHuffman=ArbolHuffman()
    unArbolHuffman.InOrden(unArbolHuffman.getraiz())
if __name__ == '__main__':
    test()