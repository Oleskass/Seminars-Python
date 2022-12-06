# 3) Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    min_num = min(arg_1, arg_2, arg_3)
    sum_num = arg_1 + arg_2 + arg_3 - min_num
    print(min_num)
    print(sum_num)


num_1 = int(input('Type first number = '))
num_2 = int(input('Type second number = '))
num_3 = int(input('Type third number = '))
my_func(num_1, num_2, num_3)
