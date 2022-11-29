# 6) *Реализовать структуру данных «Товары». Она должна представлять собой
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные
# у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
# каждый ключ — характеристика товара, например название, а значение — список
# значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

print('How many items you want to add? ')
number_of_items = int(input())
list_of_items = []
i = 0

'''Все данные вводит пользователь: '''
while i < number_of_items:
    print('Article:')
    item_article = input()
    my_dict = {'title': None, 'price': None, 'quantity': None, 'units': 'pcs.'}
    print('Title:')
    my_dict['title'] = input()
    print('Price:')
    my_dict['price'] = input()
    print('Quantity:')
    my_dict['quantity'] = input()
    item = (item_article, my_dict)
    list_of_items.append(item)
    i += 1

'''Пользователь вводит только кол-во товаров, данные сами заполняются:
while i < number_of_items:
    print('Article:')
    item_article = 3000 + i
    my_dict = {'title': None, 'price': None, 'quantity': None, 'units': 'pcs.'}
    print('Title:')
    my_dict['title'] = f'comp + {i}'
    print('Price:')
    my_dict['price'] = 50000 + i * 200
    print('Quantity:')
    my_dict['quantity'] = 15 + i
    item = (item_article, my_dict)
    list_of_items.append(item)
    i += 1'''

print('------------------------------')
print('ITEMS STRUCTURE:')
for el in list_of_items:
    print(el)

list_of_titles = []
list_of_prices = []
list_of_quantity = []
list_of_units = []
analytics = {}

print('------------------------------')
print('ITEMS ANALYTICS:')
for i in range(len(list_of_items)):
    list_of_titles.append(list_of_items[i][1]['title'])
    list_of_prices.append(list_of_items[i][1]['price'])
    list_of_quantity.append(list_of_items[i][1]['quantity'])
    list_of_units.append(list_of_items[i][1]['units'])

analytics.update({'Titles': list_of_titles, 'Prices': list_of_prices,
                  'Quantities': list_of_quantity, 'Units': set(list_of_units)})
print(analytics)
