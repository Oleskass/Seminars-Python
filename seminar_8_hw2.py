class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return self.quantity - other.quantity
        else:
            return 'Разность количества ячеек меньше нуля'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity


a1 = Cell(2500)
a2 = Cell(88)
print(a1.quantity)
print(a2.quantity)
print(f'Объединение двух клеток = {a1 + a2}')
print(f'Вычитание клеток = {a1 - a2}')
print(f'Общая клетка из двух = {a1 * a2}')
print(f'Деление клеток = {a1 / a2}')
