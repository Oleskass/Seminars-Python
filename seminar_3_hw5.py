# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма
# вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
# вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

def sum_of_numbers():
    sum_num = 0
    while True:
        input_line = input('Type numbers with space key: \n').split()
        if input_line == ['q'] or input_line == ['Q']:
            break
        for i in range(len(input_line)):
            sum_num += int(input_line[i])
        print(f'Result: {sum_num}\n(для выхода нажмите Q или q)')


sum_of_numbers()