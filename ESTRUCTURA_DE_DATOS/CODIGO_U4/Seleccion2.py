def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

my_list = [5, 3, 6, 2, 10]
idx = find_smallest(my_list)
print("El elemento más pequeño se encuentra en el índice:", idx)
