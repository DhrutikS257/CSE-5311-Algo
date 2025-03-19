def ith_quicksort(arr, i):

    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]     
    pivots = [x for x in arr if x == pivot]    
    right = [x for x in arr if x > pivot]      

    if i < len(left):
        return ith_quicksort(left, i)
    elif i < len(left) + len(pivots):
        return pivot
    else:
        return ith_quicksort(right, i - len(left) - len(pivots))


arr = [9, 3, 2, 4, 8, 6, 5]
# from 0 to n
i =  3
result = ith_quicksort(arr, i)
print(f"The {i+1}-th smallest element in {arr} is {result}")
