from ColaSecuencial import ColaSec
from ColaEnlazada import ColaEn
def test():
    max=int(input('\nIngrese cantidad de elementos de la cola: '))
    unaCola=ColaSec(max)
    for i in range(max):
        num=int(input('\nIngrese un numero a insertar en la cola: '))
        unaCola.Insertar(num)
    unaCola.Recorrer()
if __name__ == '__main__':
    test()