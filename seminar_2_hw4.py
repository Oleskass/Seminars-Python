# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

print('Введите несколько слов через пробел: ')
new_line = input().split()
for num, el in enumerate(new_line, 1):
    print(f'{num} {el:.10}')
