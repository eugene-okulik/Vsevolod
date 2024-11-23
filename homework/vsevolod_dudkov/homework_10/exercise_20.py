def func_calc(*args):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            print(first * second)
        elif first > second:
            print(first - second)
        elif first < second:
            print(first / second)
        elif first == second:
            print(first + second)

    return wrapper


@func_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        return first * second


calc(4, 5, '+')
