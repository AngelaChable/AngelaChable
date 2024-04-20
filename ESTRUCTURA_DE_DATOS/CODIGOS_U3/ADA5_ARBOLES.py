class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            pass

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierda)
        else:
            return self._buscar_recursivo(valor, nodo_actual.derecha)

    def preorden(self):
        nodos = []
        self._preorden_recursivo(self.raiz, nodos)
        return nodos

    def _preorden_recursivo(self, nodo, nodos):
        if nodo:
            nodos.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, nodos)
            self._preorden_recursivo(nodo.derecha, nodos)


arbol = Arbol()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(1)
arbol.insertar(4)

print("Preorden:", arbol.preorden())
print("¿El valor 3 está en el árbol?", arbol.buscar(3))
print("¿El valor 10 está en el árbol?", arbol.buscar(10))
