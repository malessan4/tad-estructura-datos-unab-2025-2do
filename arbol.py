class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

# Implementacion de un setter
    def insertar(self, dato):
        self.raiz = self._insertar_rec(self.raiz, dato)

    def _insertar_rec(self, nodo, dato):
        if nodo is None:
            return NodoArbol(dato)
        if dato < nodo.dato:
            nodo.izq = self._insertar_rec(nodo.izq, dato)
        else:
            nodo.der = self._insertar_rec(nodo.der, dato)
        return nodo
    
    def inorden(self):
        # Recorrido inorden (izquierda, raíz, derecha)
        resultado = self._inorden_rec(self.raiz)
        print(f"Recorrido Inorden {resultado}")
        return resultado
    
    def _inorden_rec(self, nodo):
        if nodo is None:
            return []
        resultado = self._inorden_rec(nodo.izq) + [nodo.dato] + self._inorden_rec(nodo.der)
        return resultado
    
    def mostar_raiz(self):
        print(f"La raiz es: {self.raiz.dato}")
    

# PROGRAMA PRINCIPAL
arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(4)
arbol.insertar(8)
arbol.insertar(13)
arbol.insertar(2)
arbol.insertar(35)
arbol.insertar(86)
arbol.insertar(54)
arbol.insertar(18)
arbol.mostar_raiz()
arbol.inorden()
