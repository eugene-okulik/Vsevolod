import sys

sys.set_int_max_str_digits(0)


def fibonacci(n):
    fib1, fib2 = 0, 1
    while fib2 < n:
        yield fib2
        fib1, fib2 = fib2, fib1 + fib2


f = fibonacci(float('inf'))

for i, v in enumerate(f):
    if i == 5:
        print(v)
    elif i == 200:
        print(v)
    elif i == 1000:
        print(v)
    elif i == 100000:
        print(v)
        break
