class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


data_1 = input('Введите первое число: ')
data_2 = input('Введите второе число: ')

try:
    data_1 = int(data_1)
    data_2 = int(data_2)
    if data_2 == 0:
        raise OwnError('На ноль делить нельзя!')
except ValueError:
    print('Вы ввели не число :(')
except OwnError as err:
    print(err)
else:
    res = data_1 / data_2
    print(f'{data_1} разделить на {data_2} получится {res}.')


