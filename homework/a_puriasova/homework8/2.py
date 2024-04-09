def progression():
    n = 2
    num = 1
    while True:
        yield num
        num += n


# Создаем генератор чисел Фибоначчи
fib_gen = progression()

# Получаем пятое, двухсотое, тысячное и стотысячное число Фибоначчи
fib_numbers = []

# Получаем необходимые числа Фибоначчи
for _ in range(5):
    fib_numbers.append(next(fib_gen))

for _ in range(195):
    next(fib_gen)

for _ in range(799):
    next(fib_gen)

for _ in range(99999 - 1000):
    next(fib_gen)

# Печатаем полученные числа Фибоначчи
print("Пятое число Фибоначчи:", fib_numbers[4])
print("Двухсотое число Фибоначчи:", next(fib_gen))
print("Тысячное число Фибоначчи:", next(fib_gen))
print("Сто тысячное число Фибоначчи:", next(fib_gen))
