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

'''
print('How many items you want to add? ')
number_of_items = int(input())
list_of_items = []
i = 0
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

print('------------------------------')
print(my_dict)
print('ITEMS STRUCTURE:')
for el in list_of_items:
    print(el)
'''
# analytics = {}
# for j in list_of_items:
#     # for list_of_items[my_dict.keys()], list_of_items[my_dict.values()] \
#     #         in j[1].items():
#     analytics[list_of_items[my_dict.keys()]].append(my_dict.values())
#
# print(analytics)

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
# каждый ключ — характеристика товара, например название, а значение — список
# значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],

# test_dict = {'title': 'computer', 'price': 74999, 'quantity': 9,
#              'units': 'pcs.'}
# print(test_dict.keys())

dict_1 = {'title': 'computer', 'price': 74999, 'quantity': 9,
          'units': 'pcs.'}
item_1 = (34001, {'title': 'computer', 'price': 74999, 'quantity': 9,
                  'units': 'pcs.'})
item_2 = (34002, {'title': 'phone', 'price': 56999, 'quantity': 23,
                  'units': 'pcs.'})
item_3 = (34003, {'title': 'printer', 'price': 8299, 'quantity': 6,
                  'units': 'pcs.'})
item_4 = (34004, {'title': 'headphones', 'price': 12499, 'quantity': 17,
                  'units': 'pcs.'})
list_of_items = [item_1, item_2, item_3, item_4]

print('------------------------------')
print(dict_1)
print('ITEMS STRUCTURE:')
for el in list_of_items:
    print(el)

print('--test---------------')
for i in list_of_items:
    dict_keys = [list_of_items[i][i].get('title')], \
                [list_of_items[i][i].get('price')], \
                [list_of_items[i][i].get('quantity')], \
                [list_of_items[i][i].get('units')]
    print(dict_keys)

# # {'title': 'computer', 'price': 74999, 'quantity': 9, 'units': 'pcs.'}
# print(list_of_items[0][1])
# # dict_keys(['title', 'price', 'quantity', 'units'])
# print(dict_1.keys())
# # dict_values(['computer', 74999, 9, 'pcs.'])
# print(dict_1.values())
# # dict_items([('title', 'computer'), ('price', 74999), ('quantity', 9),
# # ('units', 'pcs.')])
# print(dict_1.items())
# # computer
# print(dict_1.get('title'))
#
# # item_4for el in list_of_items:
# #     print(el[1])
#
#
# print(type(item_1[1]))  # <class 'dict'>
# print(type(item_1[0]))  # <class 'int'>
