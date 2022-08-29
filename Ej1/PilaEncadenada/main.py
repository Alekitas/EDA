from ClasePilaEncadenada import Encadenada
from clasecelda import celda


if __name__ == "__main__":
   cant=int(input('\n Ingrese cantidad de componentes de la pila:'))
   unapila=Encadenada(cant)
   for i in range(cant):
        x=int(input("\n Ingrese un numero:"))
        unapila.insertar(x)
   unapila.mostrar()
