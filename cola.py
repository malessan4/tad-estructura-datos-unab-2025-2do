class NodoCola(object):
    def __init__(self):
        self.info = None
        self.sig = None


class Cola(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def insertar(self, dato):
        nuevo_nodo = NodoCola()
        nuevo_nodo.info = dato
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
            print(f"El nodo {dato} ha sido agregado exitosamente, la cola tiene un tamanio de {self.tamanio}")
        else:
            self.ultimo.sig = nuevo_nodo
            self.ultimo = nuevo_nodo 
            self.tamanio += 1
            print(f"El nodo {dato} ha sido agregado a lo ultimo de la cola y el tamanio de la cola es {self.tamanio}")

    def desencolar(self):
        if self.primero is None:
            print("La cola esta vacia")
        else:
            dato = self.primero.info
            self.primero = self.primero.sig
            self.tamanio -= 1
            print(f"El {dato} a sido eliminado de la cola y el tamanio de la cola es {self.tamanio}")

    def mandar_a_lo_ultimo(self):
        if self.primero is None:
            print("La cola esta vacia")
        elif self.primero == self.ultimo:
            print("Hay un solo dato en la cola, imposible mandarlo a lo ultimo")
        else:
            nodo_a_mover = self.primero
            dato = nodo_a_mover.info
            self.primero = self.primero.sig
            self.ultimo.sig = nodo_a_mover
            self.ultimo = nodo_a_mover
            nodo_a_mover.sig = None
            print(f"El {dato} a sido enviado a lo ultimo de la cola")

        

    def mostrar_cola(self):
        if self.primero is None:
            print(f"La cola esta vacia")
            return
        else:
            actual = self.primero
            print(f"La cola tiene un tamanio de: {self.tamanio}")
            print("La cola es:")
            while actual is not None:
                print(f"{actual.info}")
                actual = actual.sig




mi_cola = Cola()
mi_cola.mostrar_cola()
mi_cola.insertar(5)
mi_cola.mandar_a_lo_ultimo()
mi_cola.mostrar_cola()
mi_cola.insertar(10)
mi_cola.insertar(2)
mi_cola.insertar(4)
mi_cola.mandar_a_lo_ultimo()
mi_cola.mostrar_cola()
mi_cola.desencolar()
mi_cola.mostrar_cola()
mi_cola.desencolar()
mi_cola.mostrar_cola()
mi_cola.desencolar()
mi_cola.mostrar_cola()


