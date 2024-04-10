from decimal import Decimal

def fibonacci():
    a, b = Decimal(0), Decimal(1)
    while True:
        yield a
        a, b = b, a + b

# Создаем генератор чисел Фибоначчи
fib_gen = fibonacci()

# Получаем пятое число Фибоначчи
for _ in range(5):
    next(fib_gen)
fib_5 = next(fib_gen)

# Получаем двухсотое число Фибоначчи
for _ in range(195):
    next(fib_gen)
fib_200 = next(fib_gen)

# Получаем тысячное число Фибоначчи
for _ in range(800):
    next(fib_gen)
fib_1000 = next(fib_gen)

# Печатаем полученные числа Фибоначчи
print("Пятое число Фибоначчи:", fib_5)
print("Двухсотое число Фибоначчи:", fib_200)
print("Тысячное число Фибоначчи:", fib_1000)

