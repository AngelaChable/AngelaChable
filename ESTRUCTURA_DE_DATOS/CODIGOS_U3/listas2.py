class Postres:
    def __init__(self):
        self.postres = {}

    def imprimir_ingredientes(self, nombre_postre):
        if nombre_postre in self.postres:
            print(f'Ingredientes de {nombre_postre} son: {self.postres[nombre_postre]}')
        else:
            print(f'El postre {nombre_postre} no está en la lista.')

    def agregar_ingredientes(self, nombre_postre, nuevos_ingredientes):
        if nombre_postre in self.postres:
            self.postres[nombre_postre].extend(nuevos_ingredientes)
            self.postres[nombre_postre] = list(set(self.postres[nombre_postre])) 
            print(f'Se agregaron los ingredientes a {nombre_postre}.')
        else:
            print(f'El postre {nombre_postre} no está en la lista.')

    def eliminar_ingredientes(self, nombre_postre, ingredientes_a_eliminar):
        if nombre_postre in self.postres:
            for ingrediente in ingredientes_a_eliminar:
                if ingrediente in self.postres[nombre_postre]:
                    self.postres[nombre_postre].remove(ingrediente)
            print(f'Se eliminaron los ingredientes de {nombre_postre}.')
        else:
            print(f'El postre {nombre_postre} no está en la lista.')

    def alta_postre(self, nombre_postre, ingredientes):
        if nombre_postre not in self.postres:
            self.postres[nombre_postre] = ingredientes
            print(f'Se dio de alta el postre {nombre_postre}.')
        else:
            print(f'El postre {nombre_postre} ya existe en la lista.')

    def baja_postre(self, nombre_postre):
        if nombre_postre in self.postres:
            del self.postres[nombre_postre]
            print(f'Se dio de baja el postre {nombre_postre}.')
        else:
            print(f'El postre {nombre_postre} no está en la lista.')

    def eliminar_repetidos(self):
        for postre, ingredientes in self.postres.items():
            self.postres[postre] = list(set(ingredientes))


postres = Postres()
postres.alta_postre('Pastel de Chocolate', ['Harina', 'Azúcar', 'Chocolate', 'Huevos', 'Azúcar'])
postres.alta_postre('Helado de Vainilla', ['Leche', 'Crema', 'Azúcar', 'Vainilla', 'Leche'])
postres.agregar_ingredientes('Pastel de Chocolate', ['leche entera', 'leche entera'])
postres.eliminar_repetidos()
postres.baja_postre('Helado de Vainilla')
print(postres.postres)
