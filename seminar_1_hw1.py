# 1) Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

a = 15
b = 4.11
c = 'Hello world'
d = True
e = [5, 12, 28, 37, 50]
f = (0, 1, 2)
g = {'name': 'Vasiliy', 'age': 40, 'height': 180}
print(f'{a}\n{b}')
print('{}\n{}'.format(c, d))
print(e)
print(f)
print(g)
print(f'{type(a)}\n{type(b)}\n{type(c)}\n{type(d)}'
      f'\n{type(e)}\n{type(f)}\n{type(g)}')

print()
print('Как вас зовут? ')
name = input()
print('Какого числа у вас день рождения? ')
date = int(input())
print('Введите любимое число: ')
number = int(input())
print('Введите любое слово: ')
random_word = input()

print(f'Имя: {name}')
print(f'Число дня рождения: {date} и любимое число: {number}')
print(f'Ваше слово: {random_word}')
