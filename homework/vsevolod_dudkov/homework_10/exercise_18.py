def universal(func):
    def wrapper():
        func()
        print('finished')

    return wrapper


@universal
def print_me():
    print('print me')


print_me()
