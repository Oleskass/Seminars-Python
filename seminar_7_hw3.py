# 3) Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход). Последний
# атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера
# на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = None
    surname = None
    position = None
    wage = 0
    bonus = 0
    _income = {}

    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}, {self.position}')

    def get_total_income(self):
        print(
            f'Income = {self._income.get("wage") + self._income.get("bonus")}\n')


obj_1 = Position('Ivan', 'Petrov', 'Photographer', 85000, 25000)
obj_1.get_full_name()
obj_1.get_total_income()

obj_2 = Position('Anna', 'Ivanova', 'Economist', 115000, 30000)
obj_2.get_full_name()
obj_2.get_total_income()

print(obj_1.name)
print()
print(obj_2.position)
