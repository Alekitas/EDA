from ClasePila import Pila
import numpy as np
def test():
    cant=int(input('Ingrese cantidad de elementos a usar: '))
    Pila1=Pila(cant)
    Pila2=Pila(cant)
    Pila3=Pila(cant)

    cantmov=0

    Arre=[Pila1,Pila2,Pila3]

    for i in range(len(Arre)):
        Arre[0].Insertar(cant)
        cant-=1
    
    for i in range(len(Arre)):
        print('Torre {}\n'.format(i+1))
        Arre[i].Mostrar()
    
    while not Arre[2].llena():
        origen=int(input('\nIngrese la torre origen: '))
        destino=int(input('\nIngrese la torre destino: '))

        if not Arre[origen-1].vacia():
            if (Arre[destino-1].vacia() or Arre[origen-1].Ultimo() < Arre[destino-1].Ultimo()):
                Arre[destino-1].Insertar(Arre[origen-1].Suprimir())
                cantmov+=1

            for i in range(len(Arre)):
                print('\nTorre: {}'.format(i+1))
                Arre[i].Mostrar()
            else:
                print('La ultima ficha de la Torre {} es mas pequeña que la ultima ficha de la Torre {}'.format(origen,destino))
        
        else:
            print('Torre {}'.format(origen))
                

if __name__ == '__main__':
    test()