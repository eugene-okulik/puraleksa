# с использованием метода index
results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for result in results:
    number_str = result[result.index(":") + 2:]
    number = int(number_str)
    print(number + 10)

print()
print()

# с использованием метода split()
results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for result in results:
    number_str = result.split(":")[-1].strip()
    number = int(number_str)
    print(number + 10)
