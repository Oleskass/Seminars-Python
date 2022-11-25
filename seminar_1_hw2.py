# 2) Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print('Введите время в секундах: ')
sec_input = int(input())
seconds = sec_input % 60
hours = sec_input // 3600
minutes = sec_input // 60 - hours * 60
time = f'Секунды в чч:мм:сс: \n{hours:02}:{minutes:02}:{seconds:02}'
print(time)
