# 7)* Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример: 6782 -> 23, 0,56 -> 11

print('Введите вещественное число через точку (не более 5 цифр после точки):')
number = float(input())
digit_sum = None
dig_sum_1 = 0
dig_sum_2 = 0

a = int(number)
b = number - a
i = 0
if a != 0:
    while a >= 1:
        dig_sum_1 += a % 10
        a //= 10
        i += 1

if b != 0:
    b = round(b, 5) * 100000
    while b >= 1:
        dig_sum_2 += b % 10
        b //= 10
        i += 1

digit_sum = round(dig_sum_1 + dig_sum_2)

print(f'Сумма цифр вещественного числа: {digit_sum}')
