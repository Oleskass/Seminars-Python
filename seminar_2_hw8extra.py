# 7)* Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Введите число N:')
number_n = int(input())
mult_list = []
mult = 1

for i in range(1, number_n + 1):
    mult *= i
    mult_list.append(mult)

print(mult_list)
