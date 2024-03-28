# Заданные списки студентов и предметов
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Форматирование текста с использованием данных из списков
text = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"
print(text)


# Форматирование текста с использованием данных из списков
text = "Students {}, {}, {} study these subjects: {}, {}, {}".format(students[0], students[1], students[2],
                                                                     subjects[0], subjects[1], subjects[2])
print(text)
