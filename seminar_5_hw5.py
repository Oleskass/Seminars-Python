# 5) Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел
# в файле и выводить ее на экран.

with open('file5.txt', 'w', encoding='utf-8') as data:
    for x in range(1, 21):
        data.writelines(f'{x} ')

with open('file5.txt', 'r', encoding='utf-8') as data:
    numbers = data.read().split()
    num_sum = sum(map(int, numbers))
    print(num_sum)


