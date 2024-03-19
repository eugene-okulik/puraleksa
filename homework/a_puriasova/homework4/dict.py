my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'},
    'set': {100, 200, 300, 400, 500}
}

# Для ключа 'tuple'
print("Последний элемент кортежа:", my_dict['tuple'][-1])

# Для ключа 'list'
my_dict['list'].append(60)  # Добавляем элемент в конец списка
my_dict['list'].pop(1)      # Удаляем второй элемент списка
print("Измененный список:", my_dict['list'])

# Для ключа 'dict'
my_dict['dict']['i am a tuple'] = 'value6'  # Добавляем новый элемент
my_dict['dict'].pop('key1')  # Удаляем элемент с ключом 'key1'
print("Измененный словарь:", my_dict['dict'])

# Для ключа 'set'
my_dict['set'].add(600)   # Добавляем новый элемент в множество
my_dict['set'].pop()    # Удаляем произвольный элемент из множества
print("Измененное множество:", my_dict['set'])

# Выводим на экран весь словарь
print("Весь словарь:", my_dict)
