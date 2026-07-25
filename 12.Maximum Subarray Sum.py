arr = [-2, -3, 4, -1, -2, 1, 5, -3]

current = maximum = arr[0]

for i in arr[1:]:
    current = max(i, current + i)
    maximum = max(maximum, current)

print("Maximum Subarray Sum =", maximum)