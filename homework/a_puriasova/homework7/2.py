words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, count in words.items():
    print(word * count)
print()

# другой вариант
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

output = [word * count for word, count in words.items()]
print('\n'.join(output))
print()

# третий варинт
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, count in words.items():
    print(f"{word * count}")
