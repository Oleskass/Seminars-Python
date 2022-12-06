# 4) Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения
# числа в степень. Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора возведения в степень.
# Второй — более сложная реализация без оператора возведения в степень,
# предусматривающая использование цикла.

def my_func(x, y):
    if y < 0 < x:
        result = x ** y
        print(result)
    else:
        print('Ошибка, попробуйте ввести другие значения.')


def my_func2(x, y):
    if y < 0 < x:
        result = 1
        for i in range(y * -1):
            result *= 1 / x
        print(result)
    else:
        print('Ошибка, попробуйте ввести другие значения.')


num_x = float(input('Введите положительное число: '))
num_y = int(input('Введите целое отрицательное число: '))
print('Функция my_func:')
my_func(num_x, num_y)
print('Функция my_func2:')
my_func2(num_x, num_y)
