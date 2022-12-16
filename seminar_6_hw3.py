from timeit import timeit

list_1 = [234, 55, 3, 4, 32, 65, 43, 315, 20, 1, 6]


def my_func_3():
    max_n = list_1[0]
    for el in list_1:
        if el > max_n:
            max_n = el
    return max_n


def my_func_4():
    max_num = max(list_1)
    return max_num


'''
Так как из своих кодов я не нашла особо показательных, решила написать ещё 
отдельный код и замерить его. В первой функции находим максимальное число в
списке через цикл, времени затратили на это 0.037051, во второй функции - 
через встроенную функцию max, что заняло времени 0.029731, это быстрее, 
чем у первого кода.
Таким образом:
my_func_3() - 0.037051
my_func_4() - 0.029731
'''

print(
    timeit("my_func_3()", globals=globals(), number=100000))
# 0.037051

print(
    timeit("my_func_4()", globals=globals(), number=100000))
# 0.029731
