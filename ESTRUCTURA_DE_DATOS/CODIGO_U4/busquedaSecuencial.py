def sequential_search(arr, target):

    for item in arr:
        if item == target:
            return True
    return False

arr = [3, 5, 1, 9, 2, 7, 6, 8, 4]
target = 7
if sequential_search(arr, target):
    print(f"El elemento {target} se encuentra en el arreglo.")
else:
    print(f"El elemento {target} no se encuentra en el arreglo.")
