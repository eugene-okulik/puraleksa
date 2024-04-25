class Book:
    def __init__(self, material, has_text, title, author, num_pages, isbn, reserved):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = reserved


class Textbook(Book):
    def __init__(self, material, has_text, title, author, num_pages, isbn, reserved, subject, grade, has_exercises):
        super().__init__(material, has_text, title, author, num_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises


# Создание экземпляров книг
book1 = Book("бумага", True, "Идиот", "Достоевский", 500, "1234567890", False)
book2 = Book("бумага", True, "Преступление и наказание", "Достоевский", 600, "0987654321", True)
book3 = Book("электронный", True, "1984", "Джордж Оруэлл", 350, "5678901234", False)
book4 = Book("бумага", True, "Война и мир", "Лев Толстой", 1000, "4321098765", False)
book5 = Book("электронный", True, "Гарри Поттер и философский камень", "Дж. К. Роулинг", 400, "9876543210", False)

# Создание экземпляров учебников
textbook1 = Textbook("бумага", True, "Алгебра", "Иванов", 200, "1234567890", False, "Математика", 9, True)
textbook2 = Textbook("бумага", True, "История", "Петров", 150, "0987654321", True, "История", 10, False)
textbook3 = Textbook("бумага", True, "География", "Сидоров", 180, "5678901234", False, "География", 8, True)
textbook4 = Textbook("бумага", True, "Физика", "Смирнов", 250, "4321098765", False, "Физика", 11, False)
textbook5 = Textbook("бумага", True, "Литература", "Козлова", 220, "9876543210", False, "Литература", 7, True)

# Пометка одной книги и одного учебника как зарезервированных
book2.reserved = True
textbook2.reserved = True

# Печать деталей о каждой книге
books = [book1, book2, book3, book4, book5]
for book in books:
    if book.reserved:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, "
              f"материал: {book.material}, зарезервирована")
    else:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, "
              f"материал: {book.material}")

# Печать деталей о каждом учебнике
textbooks = [textbook1, textbook2, textbook3, textbook4, textbook5]
for textbook in textbooks:
    if textbook.reserved:
        print(f"Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.num_pages}, "
              f"материал: {textbook.material}, предмет: {textbook.subject}, класс: {textbook.grade}, зарезервирована")
    else:
        print(f"Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.num_pages}, "
              f"материал: {textbook.material}, предмет: {textbook.subject}, класс: {textbook.grade}")
