def fibonacci(limit):
    fib_numbers = []
    a, b = 0, 1
    count = 0
    while count < limit:
        fib_numbers.append(a)
        a, b = b, a + b
        count += 1
    return fib_numbers


fib_numbers_5 = fibonacci(5)
print("Пятое число Фибоначчи:", fib_numbers_5[4])

fib_numbers_200 = fibonacci(200)
print("Двухсотое число Фибоначчи:", fib_numbers_200[199])

fib_numbers_1000 = fibonacci(1000)
print("Тысячное число Фибоначчи:", fib_numbers_1000[999])

# fib_numbers = fibonacci(100000)
# print("Сто тысячное число Фибоначчи:", fib_numbers[99999])
# последнее уронит весь код, поэтому под комментарием, честно не нашла решения как это сделать((
