def binary(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return binary(arr, low, mid - 1, key)
        else:
            return binary(arr, mid + 1, high, key)

    return -1

arr = [5, 10, 15, 20, 25]
key = 20

result = binary(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Key found at index", result)
else:
    print("Key not found")