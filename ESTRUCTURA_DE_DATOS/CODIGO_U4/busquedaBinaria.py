def binary_search(arr, target):
    left = 0  
    right = len(arr) - 1  
    
    while left <= right:
        mid = (left + right) // 2  
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 13
result = binary_search(arr, target)
if result != -1:
    print(f"El elemento {target} se encuentra en la posición {result} del arreglo.")
else:
    print(f"El elemento {target} no se encuentra en el arreglo.")
