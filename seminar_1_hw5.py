# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('Введите выручку: ')
income = int(input())
print('Введите издержки фирмы: ')
expenses = int(input())
fin_result = income - expenses

if fin_result > 0:
    print(f'Фирма получает прибыль {fin_result} руб.\n')
    ros = fin_result / income * 100
    print('Введите количество сотрудников фирмы: ')
    employees = int(input())
    profit_per_person = fin_result // employees
    print(f'Рентабельность выручки: {ros:.1f} %\n'
          f'Прибыль фирмы на одного сотрудника: {profit_per_person} руб.')
else:
    print(f'Фирма получает убыток {fin_result} руб.')
