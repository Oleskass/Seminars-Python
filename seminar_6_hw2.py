from timeit import timeit

list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list_1)


def my_func_1():
    list_2 = []
    for i in range(1, len(list_1)):
        if list_1[i] > list_1[i - 1]:
            list_2.append(list_1[i])

    print(list_2)


def my_func_2():
    # print(len(list_1))
    list_2 = [list_1[i] for i in range(1, len(list_1)) if
              list_1[i] > list_1[i - 1]]

    print(list_2)


'''
Первый код - на создание списка через функцию append и цикл for, занял времени
0.046805, второй код написала с помощью list comprehension с условием и он 
занял почему-то больше времени - 0.051190. Здесь оптимизация не удалась :(
Таким образом:
my_func_1() - 0.046805
my_func_2() - 0.051190
'''

print(
    timeit("my_func_1()", globals=globals(), number=10000))
# 0.046805

print(
    timeit("my_func_2()", globals=globals(), number=10000))
# 0.051190
