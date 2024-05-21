class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.hash_table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.hash_table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None


hash_table = HashTable(10)
hash_table.insert(123, "apple")
hash_table.insert(456, "banana")
hash_table.insert(789, "orange")

print("Valor encontrado para la clave 456:", hash_table.search(456))
