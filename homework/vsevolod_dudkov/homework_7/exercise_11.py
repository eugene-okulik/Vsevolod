a = 5

while True:
    user_input = input('Введите свою цифру: ')
    if not user_input.isdigit():
        print('Попробуйте снова!')
        continue

    user_input = int(user_input)

    if user_input == a:
        print('Поздравляю! Вы угадали!')
        break
