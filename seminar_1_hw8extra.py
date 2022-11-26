# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Пользователь вводит значения x, y, z
print('Введите значения x, y, z (0 или 1) через enter:')
x = bool(input())
y = bool(input())
z = bool(input())

# Заранее заданные x, y, z
# x = True
# y = True
# z = True

expression_1 = not (x or y or z)
expression_2 = not x and not y and not z

print(expression_1 == expression_2)
