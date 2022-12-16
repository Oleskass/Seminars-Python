from timeit import timeit

month = input('Введите номер месяца (от 1 до 12): \n')


# Решение через словарь
def seasons_dictionary():
    seasons_dict = {'Зима': ('1', '2', '12'),
                    'Весна': ('3', '4', '5'),
                    'Лето': ('6', '7', '8'),
                    'Осень': ('9', '10', '11')}
    for key in seasons_dict.keys():
        if month in seasons_dict[key]:
            print(key)


# Решение через список
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
Замерила время двух написанных раннее кодов, увидела, что по времени 
выполнения кода словари отрабатывают дольше, чем списки. Этот же код решила 
реализовать через кортежи, время выполнения кода оказалось ещё меньше.
Таким образом:
seasons_dictionary() - через словарь - 0.038837
seasons_list() - через список - 0.030590
seasons_tuple() - через кортеж - 0.025063
'''

print(timeit("seasons_dictionary()", globals=globals(), number=10000))
# 0.038837
print(timeit("seasons_list()", globals=globals(), number=10000))
# 0.030590
print(timeit("seasons_tuple()", globals=globals(), number=10000))
# 0.025063
