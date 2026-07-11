def rec(n):
    if n == 0 or n == 1:
        return 1
    return n * rec(n - 1)

n = 5

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Iterative Factorial =", fact)
print("Recursive Factorial =", rec(n))