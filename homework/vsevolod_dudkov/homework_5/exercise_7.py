result_one = 'результат операции: 42'
result_two = 'результат операции: 514'
result_three = 'результат работы программы: 9'

slice_one = result_one[-2:]
sum_one = int(slice_one) + 10

slice_two = result_two[-3:]
sum_two = int(slice_two) + 10

slice_three = result_three[-1:]
sum_three = int(slice_three) + 10

print(slice_one, sum_two, sum_three)
