def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
          
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = ["banana", "apple", "cherry", "orange", "grape"]

bubble_sort_strings(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i], end=" ")
