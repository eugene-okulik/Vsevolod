def func_calc(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            func(first, second, '*')
        if first == second:
            func(first, second, '+')
        if first > second:
            func(first, second, '-')
        if first < second:
            func(first, second, '/')

    return wrapper


@func_calc
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '/':
        print(first / second)
    else:
        print(first * second)


calc(5, 5)
