from ClasePila import Pila
def test():
    cant=3
    unaPila=Pila(cant)
    for i in range(cant):
        num=int(input('\nIngrese un numero a insertar: '))
        unaPila.insertar(num)

    unaPila.mostrar()
if __name__ == '__main__':
    test()