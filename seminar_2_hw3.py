# 3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
# к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = input('Введите номер месяца (от 1 до 12): \n')

# Решение через список
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

# Решение через словарь
seasons_dict = {'Зима': ('1', '2', '12'),
                'Весна': ('3', '4', '5'),
                'Лето': ('6', '7', '8'),
                'Осень': ('9', '10', '11')}
for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(key)
