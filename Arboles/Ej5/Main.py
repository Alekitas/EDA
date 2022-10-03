from MonticuloBinario import Monticulo

def test():
    unMonticulo=Monticulo(10)
    unMonticulo.insertar(3)
    unMonticulo.insertar(2)
    unMonticulo.insertar(4)
    unMonticulo.mostrar()
if __name__ == '__main__':
    test()