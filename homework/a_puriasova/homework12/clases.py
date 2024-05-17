from abc import ABC, abstractmethod


class Flower(ABC):
    def __init__(self, name, color, freshness, stem_length, price, lifespan):
        self.name = name
        self.color = color
        self.freshness = freshness  # Оценка свежести от 1 до 10
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan  # Время жизни цветка в днях

    @abstractmethod
    def __str__(self):
        pass


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, price):
        super().__init__("Роза", color, freshness, stem_length, price, lifespan=7)

    def __str__(self):
        return (f"Rose(color={self.color}, freshness={self.freshness}, stem_length={self.stem_length}, "
                f"price={self.price})")


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, price):
        super().__init__("Лилия", color, freshness, stem_length, price, lifespan=10)

    def __str__(self):
        return (f"Lily(color={self.color}, freshness={self.freshness}, stem_length={self.stem_length}, "
                f"price={self.price})")


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, price):
        super().__init__("Тюльпан", color, freshness, stem_length, price, lifespan=5)

    def __str__(self):
        return (f"Tulip(color={self.color}, freshness={self.freshness}, stem_length={self.stem_length}, "
                f"price={self.price})")


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def bouquet_cost(self):
        return sum(flower.price for flower in self.flowers)

    def average_wilting_time(self):
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def search_by_color(self, color):
        return [flower for flower in self.flowers if flower.color == color]

    def search_by_average_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]

    def search_by_parameter(self, **kwargs):
        results = self.flowers
        for key, value in kwargs.items():
            if key == "color":
                results = [flower for flower in results if flower.color == value]
            elif key == "freshness":
                results = [flower for flower in results if flower.freshness == value]
            elif key == "stem_length":
                results = [flower for flower in results if flower.stem_length == value]
            elif key == "price":
                results = [flower for flower in results if flower.price == value]
            elif key == "lifespan":
                results = [flower for flower in results if flower.lifespan == value]
        return results


# Пример использования:

# Создаем цветы
rose_red = Rose("красный", 8, 30, 100)
rose_white = Rose("белый", 9, 25, 120)
lily_yellow = Lily("желтый", 7, 40, 80)
tulip_red = Tulip("красный", 6, 35, 60)

# Создаем букет и добавляем в него цветы
bouquet = Bouquet()
bouquet.add_flower(rose_red)
bouquet.add_flower(rose_white)
bouquet.add_flower(lily_yellow)
bouquet.add_flower(tulip_red)

# Определяем стоимость букета
print("Стоимость букета:", bouquet.bouquet_cost())

# Определяем среднее время увядания букета
print("Среднее время увядания букета:", bouquet.average_wilting_time())

# Сортируем цветы в букете по цене и выводим результат
bouquet.sort_by_price()
print("Отсортированные цветы по цене:")
for flower in bouquet.flowers:
    print(flower)

# Поиск цветов в букете по цвету
yellow_flowers = bouquet.search_by_color("желтый")
print("Желтые цветы в букете:")
for flower in yellow_flowers:
    print(flower)

# Поиск цветов в букете по среднему времени жизни
flowers_with_lifespan_7 = bouquet.search_by_average_lifespan(7)
print("Цветы с временем жизни 7 дней:")
for flower in flowers_with_lifespan_7:
    print(flower)

# Поиск цветов по нескольким параметрам
search_results = bouquet.search_by_parameter(color="красный", freshness=8)
print("Цветы с параметрами (цвет='красный', свежесть=8):")
for flower in search_results:
    print(flower)
