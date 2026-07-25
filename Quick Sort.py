def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick(left) + [pivot] + quick(right)

arr = [10, 7, 8, 9, 1, 5]
print("Sorted Array:", quick(arr))