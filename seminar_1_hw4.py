# 4) Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

print('Введите целое положительное число: ')
number = input()
max_digit = number[0]
i = 1
while i < len(number):
    if number[i] > max_digit:
        max_digit = number[i]
    i += 1
print(f'Максимальная цифра в числе: {max_digit}')

# необязательно же введённые данные переводить из str в int?
# для сравнения ведь и так всё корректно работает