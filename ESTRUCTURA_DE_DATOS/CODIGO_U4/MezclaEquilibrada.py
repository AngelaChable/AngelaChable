def balanced_merge_sort(arr):
    sublists = [[x] for x in arr]
    while len(sublists) > 1:
        new_sublists = []
        for i in range(0, len(sublists), 2):
            if i + 1 < len(sublists):
                new_sublists.append(merge(sublists[i], sublists[i + 1]))
            else:
                new_sublists.append(sublists[i])
        sublists = new_sublists
    
    return sublists[0]

def merge(arr1, arr2):
    merged_arr = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1
    
    return merged_arr

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = balanced_merge_sort(arr)
print("Arreglo ordenado:", sorted_arr)
