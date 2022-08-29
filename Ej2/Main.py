from ast import Num
from ClasePila import Pila
def test():
    num=float(input=('Ingrese un numero decimal: '))
    while num>1:
        cant+=1
        num=num%2
    Binario=Pila(cant)
    while num>1:
        Binario.insertar(num)

if __name__ == '__main__':
    test()