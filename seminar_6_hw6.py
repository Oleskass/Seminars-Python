from memory_profiler import profile


@profile
def my_func_1():
    a = [1] * (10 ** 5)
    b = [2] * (2 * 10 ** 7)
    return a


@profile
def my_func_2():
    a = [1] * (10 ** 5)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


'''
Замеры памяти, профилирование.
Здесь решила написать просто отдельный код, чтобы последить, как работает 
память. Плюс здесь уже больше числа, которые и занимают больше памяти.
В первой функции мы не удалили большое (притом неиспользуемое) число b, 
во второй же функции мы высвободили это место.
'''

my_func_1()
my_func_2()

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     17.9 MiB     17.9 MiB           1   @profile
    18                                         def my_func_1():
    19     18.6 MiB      0.8 MiB           1       a = [1] * (10 ** 5)
    20    171.2 MiB    152.6 MiB           1       b = [2] * (2 * 10 ** 7)
    21    171.2 MiB      0.0 MiB           1       return a
'''

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24     18.7 MiB     18.7 MiB           1   @profile
    25                                         def my_func_2():
    26     18.7 MiB      0.0 MiB           1       a = [1] * (10 ** 5)
    27    171.2 MiB    152.6 MiB           1       b = [2] * (2 * 10 ** 7)
    28     18.7 MiB   -152.6 MiB           1       del b
    29     18.7 MiB      0.0 MiB           1       return a
'''
