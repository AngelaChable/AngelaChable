def insertion_sort_key(arr):
    return sorted(arr, key=lambda x: x)


arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort_key(arr)
print("Arreglo ordenado por inserción:", sorted_arr)
