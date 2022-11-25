a = [1, 2, 3]
b = a
print(a is b)  # true

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # false

print(f'Array is {a}')

i = 0
while True:
    i += 1
    if i >= 10:
        # инструкция break немедленно заканчивает выполнение цикла
        break
    if i % 2 == 0:
        # переходим к проверке условия цикла,
        # пропуская все операторы за инструкцией (если чётное - пропускаем!)
        continue
    # напечатаются только нечётные числа с 1 до 10
    print(i)


msg = True
if msg == True:
    print("Hello")
# Expression can be simplified (выражение мб упрощено)

msg = True
if msg:
    print("Hello2")

msg = True
if not msg:
    print("Hello3")
# здесь False
