class Nodo(object):
    info = None
    sig = None

class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0

    def insertar(self, dato):
        nuevo_nodo = Nodo()
        nuevo_nodo.info = dato
        if (self.inicio is None) or (self.inicio.info > dato):
            nuevo_nodo.sig = self.inicio # Primero engancho mi nuevo nodo al inicio actual
            self.inicio = nuevo_nodo # Ahora etiqueto a mi nuevo nodo como inicio
        else: # Si la lista no está vacía y el dato es mayor que el primer elemento
            anterior = self.inicio # se crea la variable anterior que apunta al inicio
            actual = self.inicio.sig # se crea la variable actual que apunta al nodo que venia después del inicio
            while (actual is not None) and (actual.info < dato): # si actual es None es porque llegamos al final de la lista
                anterior = actual # mientras estoy en el while, nuestro anterior ahora pasa a ser nuestro actual
                actual = actual.sig # mientras siga el while, nuestro actual pasa a ser el siguiente del actual.
            anterior.sig = nuevo_nodo # salgo del while y mi anterior.sig ahora apunta a mi nuevo nodo
            nuevo_nodo.sig = actual # y mi nuevo nodo.sig apunta a mi actual
        self.tamaño = self.tamaño + 1
