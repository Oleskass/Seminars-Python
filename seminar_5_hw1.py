# 1) Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

with open('file.txt', 'w', encoding='utf-8') as data:
    while True:
        new_text = input()
        data.write(f'{new_text}\n')
        if new_text == '':
            break
