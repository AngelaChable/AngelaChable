class Pila:
    def __init__(self, capacidad_maxima):
        self.items = []
        self.capacidad_maxima = capacidad_maxima

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        return len(self.items) == self.capacidad_maxima

    def insertar(self, elemento):
        if self.esta_llena():
            print("Error: Desbordamiento de la pila")
            return
        self.items.append(elemento)
        print(f"Insertado: {elemento}")
        self.mostrar_pila()
    
    def eliminar(self, identificador):
        if self.esta_vacia():
            print("Error: Subdesbordamiento de la pila")
            return
        for i in range(len(self.items)-1, -1, -1):
            if self.items[i] == identificador:
                eliminado = self.items.pop(i)
                print(f"Eliminado: {eliminado}")
                self.mostrar_pila()
                return
        print(f"Error: Elemento '{identificador}' no encontrado en la pila")

    def mostrar_pila(self):
        print("Estado actual de la pila:", self.items)


pila = Pila(8)

pila.insertar('X')
pila.insertar('Y')
pila.eliminar('Z')
pila.eliminar('T')
pila.eliminar('U')
pila.insertar('V')
pila.insertar('W')
pila.eliminar('p')
pila.insertar('R')
