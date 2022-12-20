# 3) Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто
# из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('file3.txt', 'r', encoding='utf-8') as data:
    name, salary = [], []
    list_1 = data.read().split('\n')
    for i in list_1:
        i = i.split()
        if int(i[1]) < 20000:
            name.append(i[0])
        salary.append(i[1])
salary_average = sum(map(int, salary)) / len(salary)
print(f'Оклад менее 20000 у: {name}')
print(f'Средняя величина окладов: {salary_average}')