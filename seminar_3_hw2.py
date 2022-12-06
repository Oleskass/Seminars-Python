# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.

def personal_data(email, lastname, name, year, city, phone):
    print(f'\nДанные пользователя:\n{name}, {lastname}, {email}, {year}, '
          f'{phone}, {city}')


personal_data(lastname=input('Введите вашу фамилию: '),
              name=input('Введите ваше имя: '),
              year=input('Какого вы года рождения? '),
              city=input('Введите ваш город: '),
              email=input('Введите email: '),
              phone=input('Введите ваш номер телефона: '))

# Реализовала двумя способами, вот второй:

# def personal_data(**kwargs):
#     print(kwargs)
#
#
# personal_data(lastname=input('Введите вашу фамилию: '),
#               name=input('Введите ваше имя: '),
#               year=input('Какого вы года рождения? '),
#               city=input('Введите ваш город: '),
#               email=input('Введите email: '),
#               phone=input('Введите ваш номер телефона: '))
