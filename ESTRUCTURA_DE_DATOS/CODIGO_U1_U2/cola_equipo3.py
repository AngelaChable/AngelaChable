from queue import Queue

cola = Queue()

cola.put(10)
cola.put(20)
cola.put(30)
cola.put(55)
cola.put(700)

elemento1 = cola.get()
elemento2 = cola.get()
elemento3 = cola.get()
elemento4 = cola.get()
elemento3 = cola.get()


print(f"Elemento extraído 1: {elemento1}")
print(f"Elemento extraído 2: {elemento2}")
print(f"Elemento extraído 3: {elemento3}")
print(f"Elemento extraído 4: {elemento4}")
print(f"Elemento extraído 3: {elemento3}")