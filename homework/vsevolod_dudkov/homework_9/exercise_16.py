import datetime

my_data = "Jan 15, 2023 - 12:05:33"
pyth_data = datetime.datetime.strptime(my_data, '%b %d, %Y - %H:%M:%S')

print(pyth_data.strftime('%B'))
print(pyth_data.strftime('%d.%m.%Y, %H:%M'))
