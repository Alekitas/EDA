class Pila:
    __cant=None
    __tope=None
    __elementos=None

    def __init__(self,cant=0):
        self.__elementos=[]
        self.__cant=cant
        self.__tope=-1

    def vacia(self):
        return self.__tope == -1
    
    def llena(self):
        return self.__tope+1 == self.__cant

    def insertar(self,obj):
        if(self.__tope<self.__cant):
            self.__tope+=1
            self.__elementos.append(obj)
            return(obj)
        else:
            return (0)

    def suprimir(self):
        if(self.vacia()):
            print('Pila vacia')
            return (0)
        else:
            self.__tope-=1
            obj=self.__elementos.pop(self.__tope)
            return obj

    def mostrar (self):
        if not (self.vacia()):
            i = self.__tope
            while (i >= 0):
                print(self.__elementos[i])
                i -= 1

    '''def mostrar(self):
        if not(self.vacia()):
            while(self.__tope>=0):
                print('Elemento: {}'.format(self.suprimir()))'''