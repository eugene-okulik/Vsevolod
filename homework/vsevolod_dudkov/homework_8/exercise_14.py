import random

salary = int(input())
bonus = bool(random.randint(0, 2))
rand_bonus = random.randint(0, 100)

res = 0
if bonus:
    res = salary + rand_bonus
else:
    res = salary

print(f'{salary}, {bonus} - ${res}')
