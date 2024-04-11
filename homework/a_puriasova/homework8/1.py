from random import choice

# Запрос у пользователя значения salary
salary = int(input("Введите вашу заработную плату (salary): "))

# Генерация случайного значения для bonus
bonus = choice([True, False])

# Если bonus - true, добавляем рандомный бонус к salary
if bonus:
    salary += choice(range(100, 1000))

# Вывод результата
print(f"Ваша заработная плата: ${salary}")
