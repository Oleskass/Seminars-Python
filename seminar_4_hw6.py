# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
# внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
# предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении
# числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import cycle, count


def count_func(num_start, num_end):
    for i in count(num_start):
        if i < num_end:
            print(i)
        else:
            break


def cycle_func(list_1, cycle_num):
    i = 0
    for el in cycle(list_1):
        if i < cycle_num * len(list_1):
            print(el)
            i += 1
        else:
            break


count_func(num_start=int(input("Enter start number: ")),
           num_end=int(input("Enter stop number: ")) + 1)
cycle_func(list_1=[17, 13, 2, 8, 9, 40],
           cycle_num=int(input("Enter quantity of cycles: ")))
