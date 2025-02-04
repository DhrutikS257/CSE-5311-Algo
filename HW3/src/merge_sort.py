def merge(arr, left, mid, right):

    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    i = 0
    j = 0

    for k in range(left, right+1):
        if i >= len(left_arr):
            arr[k] = right_arr[j]
            j += 1
        elif j >= len(right_arr):
            arr[k] = left_arr[i]
            i += 1
        elif left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

if __name__ == '__main__':
    arr = [5,2,4,7,1,3,2,6]
    print(f'Original array: {arr}')
    merge_sort(arr,0,len(arr)-1)
    print(f'Sorted array: {arr}')