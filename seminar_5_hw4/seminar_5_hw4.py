# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться
# на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('file4.txt', 'r', encoding='utf-8') as data:
    for line in data:
        line = line.strip()
        print(line)
        for i in rus_dict:
            if line.startswith(i):
                new_line = line.replace(i, rus_dict[i])
                new_file = open('file4_new.txt', 'a', encoding='utf-8')
                new_file.write(new_line + '\n')
        new_file.close()
