    def Suprimir (self, subraiz, clave, ant=None):
        if subraiz == None:
            print("\nOperacion a suprimir no es valida!")
            return None
        else:
            #si queremos eliminar la raiz del arbol (o cualquier subraiz primera pasada)
            if subraiz.getClave() == clave:
                #PRIMER CASO: si la raiz del arbol es lo q queremos eliminar, y no tiene hijos  (grado 0)
                if subraiz.getDerecha() == None and subraiz.getIzquierda() == None:
                    aux = self.__raiz
                    self.__raiz = None      #queda vacia
                    return aux
                    #SI el padre tenia un enlace por la derecha o izq, vaciamos ese enlace
                    if ant.getDerecha() == subraiz:
                        ant.setDerecha(None)
                    else:
                        ant.setIzquierda(None)
                    del subraiz

                #SEGUNDO CASO: si la raiz del arbol tiene hijo pero solo ala derecha            #a partir de aqui, grado 1 o mas
                elif subraiz.getDerecha() != None and subraiz.getIzquierda() == None:
                    hijo = subraiz.getDerecha()
                    print(f"\n1Ant: {ant.getClave()} - Subraiz: {subraiz.getClave()} - Hijo: {hijo.getClave()}")
                    if ant.getDerecha() != None:
                        ant.setIzquierda(hijo)
                    else:
                        ant.setDerecha(hijo)            #subraiz ant coloca el hijo del hijo de la raiz a la derecha """
                    ant.setDerecha(hijo)                #coloco en el anterior a eliminar, el hijo izq del eliminado, q es != None

                    return subraiz

                #TERCER CASO: si la raiz del arbol tiene hijo pero solo ala izquierda
                elif subraiz.getDerecha() == None and subraiz.getIzquierda() != None:
                    hijo = subraiz.getIzquierda()
                    print(f"\nAnt: {ant.getClave()} - Subraiz: {subraiz.getClave()} - Hijo: {hijo.getClave()}")

                    if ant.getIzquierda() != None:      #evaluo esto si el anterior tiene subraiz izq o derecha
                        ant.setDerecha(hijo)            #subraiz ant coloca el hijo del hijo de la raiz a la derecha
                    else:
                        ant.setIzquierda(hijo)
                    ant.setIzquierda(hijo)               #coloco en el anterior a eliminar, el hijo izq del eliminado, q es != None

                    return subraiz

                #CUARTO CASO: si la raiz del arbol tiene hijos en ambos lados                   (NODO DE GRADO 2)
                elif subraiz.getDerecha() != None and subraiz.getIzquierda() != None:
                    #debo encontrar el nodo que reemplazara (hoja) a la subraiz eliminada
                    nodoReemplazo = self.encontrar_reemplazo(subraiz.getIzquierda())

                    #print(f"\nNodo reemplazo es {nodoReemplazo.getClave()} - Subraiz: {subraiz.getClave()}")

                    newClave = nodoReemplazo.getClave()

                    #Suprimo el nodo hoja que ahora sera la nueva raiz del subarbol
                    self.suprimir(self.__raiz,newClave)

                    #Seteo la nueva clave en el subarbol
                    subraiz.setClave(newClave)

            elif clave < subraiz.getClave():
                #busca en subraiz de arbol izquierdo
                self.suprimir (subraiz.getIzquierda(),clave,subraiz)
            elif clave > subraiz.getClave():
                #busca en subraiz de arbol derecho
                self.suprimir (subraiz.getDerecha(), clave, subraiz)
