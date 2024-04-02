text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = text.split()
result = []

for word in words:
    if word[-1] in [',', '.']:
        result.append(word[:-1] + 'ing' + word[-1])
    else:
        result.append(word + 'ing')

result_text = ' '.join(result)
print(result_text)
