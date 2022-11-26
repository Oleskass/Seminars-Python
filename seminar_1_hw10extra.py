# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти: ')
quarter = input()

if quarter == '1':
    result = 'x > 0 и y > 0'
elif quarter == '2':
    result = 'x < 0 и y > 0'
elif quarter == '3':
    result = 'x < 0 и y < 0'
elif quarter == '4':
    result = 'x > 0 и y < 0'
else:
    result = '----'

print(f'В этой четверти находятся точки в следующем диапазоне: {result}')
