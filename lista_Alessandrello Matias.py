class Nodo(object): # se crea la clase nodo, con su informacion en None y el puntero siguiente tambien en Noe
    info = None
    sig = None

class Lista(object): #Se crea la clase lista, con su puntero inicio en None y su tamaño en 0
    def __init__(self):
        self.inicio = None
        self.tamaño = 0

    def insertar(self, dato): # Metodo de Lista para insertar un nodo de forma ordenada de menor a mayor
        nuevo_nodo = Nodo() # mi nuevo nodo es una instancia nueva de la clase Nodo
        nuevo_nodo.info = dato # mi nodo.info del nuevo nodo es igual al dato
        if (self.inicio is None) or (self.inicio.info > dato): # si la lista esta vacía o el dato es menor que el primer elemento
            nuevo_nodo.sig = self.inicio # Primero engancho mi nuevo nodo al inicio actual
            self.inicio = nuevo_nodo # Ahora etiqueto a mi nuevo nodo como inicio
        else: # Si la lista no está vacía o el dato es mayor que el primer elemento
            anterior = self.inicio # se crea la variable anterior que apunta al inicio
            actual = self.inicio.sig # se crea la variable actual que apunta al nodo que venia después del inicio
            while (actual is not None) and (actual.info < dato): # si actual es None es porque llegamos al final de la lista
                anterior = actual # mientras estoy en el while, nuestro anterior ahora pasa a ser nuestro actual
                actual = actual.sig # mientras siga el while, nuestro actual pasa a ser el siguiente del actual.
            anterior.sig = nuevo_nodo # salgo del while y mi anterior.sig ahora apunta a mi nuevo nodo
            nuevo_nodo.sig = actual # y mi nuevo nodo.sig apunta a mi actual
        self.tamaño = self.tamaño + 1
        print(f"El dato {dato} fue insertado correctamente, el tamaño actual de la lista es {self.tamaño}")


    def lista_vacia(self): # Metodo para saber si la lista esta vacia
        if self.inicio is None:
            print("La lista esta vacia")
        else:
            print("La lista no esta vacia") 
        return self.inicio is None
    
    def eliminar(self, dato_a_eliminar): # Metodo para eliminar un nodo de la lista
        if self.inicio is None: # si la lista esta vacia
            print("No se encontro el dato en la lista, no se eliminó ningun elemento")
            return False

        if self.inicio.info == dato_a_eliminar: # si el dato a eliminar es el primero de la lista
            dato = self.inicio.info
            self.incio = self.incio.sig
            self.tamaño -= 1
            print(f"El dato {dato} a sido eliminado. Tamaño actual: {self.tamaño}")
            return True
        
        anterior = self.inicio
        actual = self.inicio.sig
        while (actual is not None) and (actual.info != dato_a_eliminar):
            anterior = actual
            actual = actual.sig

        if actual is None:
            print(f"No se encontro el dato '{dato_a_eliminar}' en la lista")
            return False
        else:
            anterior.sig = actual.sig
            self.tamaño -= 1
            print(f"El dato '{dato_a_eliminar}' a sido eliminado. Tamaño actual: {self.tamaño}")
            return True

lista1 = Lista() # se crea una instancia de la clase lista llamada lista1
lista1.lista_vacia() # se pregunta si la lista esta vacia
lista1.insertar(5) # se insertan datos en la lista
lista1.insertar(3)
lista1.insertar(8)
lista1.eliminar(5)
lista1.eliminar(10) # se intenta eliminar un dato que no existe en la lista
lista1.lista_vacia() # se pregunta si la lista esta vacia
