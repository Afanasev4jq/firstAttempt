import csv

# Определение класса AnimalCollection для работы с данными о животных
class AnimalCollection:
    def __init__(self):
        self.data = []  # Инициализация пустого списка для хранения данных о животных

    # Метод для загрузки данных из CSV-файла
    def load_data_from_csv(self, file_path):
        expected_fieldnames = ['№', 'Кличка', 'порода', 'возраст']

        with open(file_path) as file:
            reader = csv.DictReader(file)

            for row in reader:
                actual_fieldnames = list(row.keys())

                if actual_fieldnames != expected_fieldnames:
                    print("Ошибка в файле. Неверные поля обнаружены.")
                    return

                self.data.append(row)
    # Метод для сохранения данных в CSV-файл
    def save_data_to_csv(self, file_path):
        with open('data1.csv', mode='w', newline='') as file:  # Открытие файла для записи
            fieldnames = ['№', 'Кличка', 'порода', 'возраст']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()  # Запись заголовка в CSV
            for row in self.data:
                writer.writerow(row)  # Запись данных из списка в CSV

    # Метод для сортировки данных по кличке
    def sort_by_name(self):
        self.data = sorted(self.data, key=lambda x: x.get('Кличка', ''))

    # Метод для сортировки данных по возрасту
    def sort_by_age(self):
        self.data = sorted(self.data, key=lambda x: int(x.get('возраст', 0)))

    # Метод для фильтрации данных по возрасту
    def filter_by_age(self, age_threshold):
        self.data = [item for item in self.data if int(item.get('возраст', 0)) > age_threshold]

    # Метод для добавления новых данных о животном
    def add_animal(self, animal_data):
        self.data.append(animal_data)

    # Метод для представления объекта в виде строки
    def __repr__(self):
        return '\n'.join(map(str, self.data))

    # Блокировка прямого изменения атрибутов класса
    def __setattr__(self, key, value):
        if key == 'data':
            super().__setattr__(key, value)
        else:
            raise AttributeError("Setting attributes directly is not allowed.")

    # Метод для доступа к элементам коллекции по индексу
    def __getitem__(self, index):
        return self.data[index]

    # Статический метод - плейсхолдер для функциональности, не требующей доступа к экземпляру класса
    @staticmethod
    def static_method():
        pass

    # Метод-генератор - плейсхолдер для генерации последовательности данных
    @staticmethod
    def generator_method():
        pass

# Пример использования класса AnimalCollection
animal_collection = AnimalCollection()

# Загрузка данных из файла
animal_collection.load_data_from_csv('data1.csv')

# Сортировка данных по возрасту и вывод результата
animal_collection.sort_by_age()
print("Отсортированные данные по возрасту:")
print(animal_collection)

# Сортировка данных по кличке и вывод результата
animal_collection.sort_by_name()
print("Отсортированные данные по кличке:")
print(animal_collection)

# Фильтрация данных по возрасту > 5 и вывод результата
print('Фильтрация данных по возрасту > 5')
animal_collection.filter_by_age(5)
print(animal_collection)

# Добавление новых данных о животном
new_animal = {'№': '4', 'Кличка': 'Рекс', 'порода': 'лабрадор', 'возраст': '3'}
animal_collection.add_animal(new_animal)

# Сохранение новых данных обратно в файл
animal_collection.save_data_to_csv('data.csv')

print("Новые данные успешно сохранены в файл.")