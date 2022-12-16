from memory_profiler import profile

month = input('Введите номер месяца (от 1 до 12): \n')


# Решение через словарь
@profile
def seasons_dictionary():
    seasons_dict = {'Зима': ('1', '2', '12'),
                    'Весна': ('3', '4', '5'),
                    'Лето': ('6', '7', '8'),
                    'Осень': ('9', '10', '11')}
    for key in seasons_dict.keys():
        if month in seasons_dict[key]:
            print(key)


# Решение через список
@profile
def seasons_list():
    list_of_seasons = ['Зима', 'Весна', 'Лето', 'Осень']

    if month == '1' or month == '2' or month == '12':
        print(list_of_seasons[0])
    elif month == '3' or month == '4' or month == '5':
        print(list_of_seasons[1])
    elif month == '6' or month == '7' or month == '8':
        print(list_of_seasons[2])
    elif month == '9' or month == '10' or month == '11':
        print(list_of_seasons[3])
    else:
        print('Ошибка! Такого месяца нет, попробуйте заново')


# Решение через кортеж
@profile
def seasons_tuple():
    tuple_of_seasons = ('Зима', 'Весна', 'Лето', 'Осень')

    if month == '1' or month == '2' or month == '12':
        print(tuple_of_seasons[0])
    elif month == '3' or month == '4' or month == '5':
        print(tuple_of_seasons[1])
    elif month == '6' or month == '7' or month == '8':
        print(tuple_of_seasons[2])
    elif month == '9' or month == '10' or month == '11':
        print(tuple_of_seasons[3])
    else:
        print('Ошибка! Такого месяца нет, попробуйте заново')


'''
Замеры памяти, профилирование.
То же самое - памяти занимают одинаково... помимо этих кодов, я ещё очень 
много замерила из своих, прикольного результата так и не нашла, к сожалению
'''

seasons_dictionary()
seasons_list()
seasons_tuple()

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     8     18.0 MiB     18.0 MiB           1   @profile
     9                                         def seasons_dictionary():
    10     18.0 MiB      0.0 MiB           2       seasons_dict = {'Зима': ('1', '2', '12'),
    11     18.0 MiB      0.0 MiB           1                       'Весна': ('3', '4', '5'),
    12     18.0 MiB      0.0 MiB           1                       'Лето': ('6', '7', '8'),
    13     18.0 MiB      0.0 MiB           1                       'Осень': ('9', '10', '11')}
    14     18.0 MiB      0.0 MiB           5       for key in seasons_dict.keys():
    15     18.0 MiB      0.0 MiB           4           if month in seasons_dict[key]:
    16     18.0 MiB      0.0 MiB           1               print(key)
'''

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    20     18.0 MiB     18.0 MiB           1   @profile
    21                                         def seasons_list():
    22     18.0 MiB      0.0 MiB           1       list_of_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
    23                                         
    24     18.0 MiB      0.0 MiB           1       if month == '1' or month == '2' or month == '12':
    25                                                 print(list_of_seasons[0])
    26     18.0 MiB      0.0 MiB           1       elif month == '3' or month == '4' or month == '5':
    27     18.0 MiB      0.0 MiB           1           print(list_of_seasons[1])
    28                                             elif month == '6' or month == '7' or month == '8':
    29                                                 print(list_of_seasons[2])
    30                                             elif month == '9' or month == '10' or month == '11':
    31                                                 print(list_of_seasons[3])
    32                                             else:
    33                                                 print('Ошибка! Такого месяца нет, попробуйте заново')
'''

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37     18.0 MiB     18.0 MiB           1   @profile
    38                                         def seasons_tuple():
    39     18.0 MiB      0.0 MiB           1       tuple_of_seasons = ('Зима', 'Весна', 'Лето', 'Осень')
    40                                         
    41     18.0 MiB      0.0 MiB           1       if month == '1' or month == '2' or month == '12':
    42                                                 print(tuple_of_seasons[0])
    43     18.0 MiB      0.0 MiB           1       elif month == '3' or month == '4' or month == '5':
    44     18.0 MiB      0.0 MiB           1           print(tuple_of_seasons[1])
    45                                             elif month == '6' or month == '7' or month == '8':
    46                                                 print(tuple_of_seasons[2])
    47                                             elif month == '9' or month == '10' or month == '11':
    48                                                 print(tuple_of_seasons[3])
    49                                             else:
    50                                                 print('Ошибка! Такого месяца нет, попробуйте заново')

'''
