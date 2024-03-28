# Заданные строки с результатами операций
results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

# Первая строка
result = results[0]
result_sum = int(result[result.index(':') + 2:]) + 10
print("Результат сложения для первой операции:", result_sum)

# Вторая строка
result = results[1]
result_sum = int(result[result.index(':') + 2:]) + 10
print("Результат сложения для второй операции:", result_sum)

# Третья строка
result = results[2]
result_sum = int(result[result.index(':') + 2:]) + 10
print("Результат сложения для работы программы:", result_sum)
