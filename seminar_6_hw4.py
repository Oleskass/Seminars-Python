from memory_profiler import profile


@profile
def my_func_1():
    print('Введите желаемое количество элементов в списке: ')
    list_length = int(input())
    our_list = []
    i = 0
    print('Введите значение элементов через enter: ')

    while i < list_length:
        our_list.append(input())
        i += 1
    print(our_list)

    for j in range(0, list_length - 1, 2):
        our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]
    print(our_list)


@profile
def my_func_2():
    our_list = input('Введите значение элементов через пробел: ').split()
    print(our_list)

    for i in range(0, len(our_list) - 1, 2):
        our_list[i], our_list[i + 1] = our_list[i + 1], our_list[i]
    print(our_list)


'''
Замеры памяти, профилирование.
Первый код взят из домашки и второй код это оптимизация - хоть он и короче, но
памяти они занимают одинаково, возможно это из-за того что слишком маленькие 
данные и программе хватает небольшого количества памяти на всё.
'''

my_func_1()
my_func_2()

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     18.0 MiB     18.0 MiB           1   @profile
     5                                         def my_func_1():
     6     18.0 MiB      0.0 MiB           1       print('Введите желаемое количество элементов в списке: ')
     7     18.0 MiB      0.0 MiB           1       list_length = int(input())
     8     18.0 MiB      0.0 MiB           1       our_list = []
     9     18.0 MiB      0.0 MiB           1       i = 0
    10     18.0 MiB      0.0 MiB           1       print('Введите значение элементов через enter: ')
    11                                         
    12     18.0 MiB      0.0 MiB           6       while i < list_length:
    13     18.0 MiB      0.0 MiB           5           our_list.append(input())
    14     18.0 MiB      0.0 MiB           5           i += 1
    15     18.0 MiB      0.0 MiB           1       print(our_list)
    16                                         
    17     18.0 MiB      0.0 MiB           3       for j in range(0, list_length - 1, 2):
    18     18.0 MiB      0.0 MiB           2           our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]
    19     18.0 MiB      0.0 MiB           1       print(our_list)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    22     18.0 MiB     18.0 MiB           1   @profile
    23                                         def my_func_2():
    24     18.0 MiB      0.0 MiB           1       our_list = input('Введите значение элементов через пробел: ').split()
    25     18.0 MiB      0.0 MiB           1       print(our_list)
    26                                         
    27     18.0 MiB      0.0 MiB           3       for i in range(0, len(our_list) - 1, 2):
    28     18.0 MiB      0.0 MiB           2           our_list[i], our_list[i + 1] = our_list[i + 1], our_list[i]
    29     18.0 MiB      0.0 MiB           1       print(our_list)
'''
