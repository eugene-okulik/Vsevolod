result_one = 'результат операции: 42'
result_two = 'результат операции: 514'
result_three = 'результат работы программы: 9'

result_index_one = result_one.index(':')
slice_one = result_one[result_index_one:]
slice_one_strip = slice_one.strip(': ')
sum_one = int(slice_one_strip) + 10

result_index_two = result_two.index(':')
slice_two = result_two[result_index_two:]
slice_two_strip = slice_two.strip(': ')
sum_two = int(slice_two_strip) + 10

result_index_three = result_three.index(':')
slice_three = result_three[result_index_three:]
slice_three_strip = slice_three.strip(': ')
sum_three = int(slice_three_strip) + 10

print(sum_one, sum_two, sum_three)
