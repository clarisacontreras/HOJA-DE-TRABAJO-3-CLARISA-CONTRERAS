Version Mejorada Bubble sort 

def bubble_sort_imp(arr):

    for i in range(len(arr)):

        is_sorted = True 
        for j in range(len(arr) - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False 


        if is_sorted:
            return arr 
    
    return arr

print(bubble_sort_imp([9, -1, 2, 42, 12, -4]))
