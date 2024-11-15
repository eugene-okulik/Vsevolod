temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_temperatures = filter(lambda x: x > 28, temperatures)
temper = list(hot_temperatures)

max_temper = max(temper)
min_temper = min(temper)
aver_temper = round((sum(temper) / len(temper)), 2)

print(f'Maximum temperature - {max_temper}, Minimum temperature '
      f'- {min_temper}, Average temperature - {aver_temper}')
