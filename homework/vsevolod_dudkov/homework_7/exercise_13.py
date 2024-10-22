result_one = 'результат операции: 42'
result_two = 'результат операции: 54'
result_three = 'результат работы программы: 209'
result_four = 'результат: 2'

def sum(result, degree=10):
    index_all = result.index(':')
    slice_all = result[index_all:]
    sl_str_one = slice_all.strip(': ')
    return int(sl_str_one) + degree

print(sum(result_one))
print(sum(result_two))
print(sum(result_three))
print(sum(result_four))
