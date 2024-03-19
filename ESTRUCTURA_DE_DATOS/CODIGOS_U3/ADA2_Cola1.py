class Cola:
    def __init__(self):
        self.items = []

    def vacio(self):
        return len(self.items) == 0

    def agregar(self, elemento):
        self.items.append(elemento)

    def quitar(self):
        if not self.vacio():
            return self.items.pop(0)
        else:
            return None

    def longitud(self):
        return len(self.items)

def sumar(cola1, cola2):
    resultado = Cola()

    while not cola1.vacio() and not cola2.vacio():
        elemsum = cola1.quitar() + cola2.quitar()
        resultado.agregar(elemsum)

    while not cola1.vacio():
        resultado.agregar(cola1.quitar())
    while not cola2.vacio():
        resultado.agregar(cola2.quitar())

    return resultado

def valores_cola():
    cola = Cola()
    valores = input("Ingrese los valores separados por espacio: ").split()
    for valor in valores:
        cola.agregar(int(valor))
    return cola


print("Ingrese los valores para la primera cola.")
cola1 = valores_cola()

print("\nIngrese los valores para la segunda cola.")
cola2 = valores_cola()

resultado = sumar(cola1, cola2)

print("\nLa cola resultante es:")
while not resultado.vacio():
    print(resultado.quitar())




