"""
f(n) = f(n-1) + f(n-2)
"""

def fib_naive(n):
    if n == 0 or n == 1: return 1
    return fib_naive(n-1) + fib_naive(n-2)

f_value = fib_naive(5)
print(f_value)


def fib_dynamic(n):
    f = [0 for i in range(n+1)]
    f[0], f[1] = 1, 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[-1]

f_value = fib_dynamic(5)
print(f_value)
