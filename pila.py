class NodoPila(object):
    info = None
    sig = None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato): # tengo que pasar a que pila ingreso el dato
        nodo = NodoPila() # Creo una instancia del nodo nuevo
        nodo.info = dato # le pongo a nodo.info el dato que yo quiero
        nodo.sig = self.cima
        self.cima = nodo
        self.tamanio += 1
        print(f"Se ingreso correctamente el dato: {nodo.info} a la pila y el tamanio es: {self.tamanio}")

    def mostrar_pila(self):
        if self.cima is None:
            print("La pila esta vacia")
            return
        else:
            actual = self.cima
            print("Los datos dentro de la pila son: ")
            while actual is not None:
                print(f"{actual.info}") 
                actual = actual.sig
            


# PROGRAMA PRINCIPAL

mi_pila = Pila()
mi_pila.mostrar_pila()
mi_pila.apilar(25)
mi_pila.apilar(2)
mi_pila.apilar(43)
mi_pila.apilar(10)
mi_pila.apilar(5)
mi_pila.apilar(300)
mi_pila.mostrar_pila()

