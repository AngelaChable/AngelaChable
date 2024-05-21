class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = [(key, value)]
        else:
            self.hash_table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.hash_table[index] is not None:
            for pair in self.hash_table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

hash_table = HashTable(10)
hash_table.insert(10, "A")
hash_table.insert(25, "B")
hash_table.insert(35, "C")

print("Valor encontrado para la clave 25:", hash_table.search(25))
