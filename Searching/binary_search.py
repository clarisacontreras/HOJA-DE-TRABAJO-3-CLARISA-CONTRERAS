def binary_search(arr, x):
    min = 0
    alt = len(arr) - 1
    med = 0
 
    while min <= alt:
 
        med = (alt + min) // 2
 
        if arr[med] < x:
            min = med + 1
 
        elif arr[med] > x:
            alt = med - 1
 
        else:
            return med
 
    return -1
