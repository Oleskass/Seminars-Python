# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


my_data = open('file2.txt', 'r')
content = my_data.read()
print(content)
print()

my_data = open('file2.txt', 'r')
lines = 0
words = 0
for line in my_data:
    lines += 1
    words += len(line.split())
    print(f'Слов в строке {lines} - {words}')
    words = 0

print(f'\nКоличество строк: {lines}')

my_data.close()



