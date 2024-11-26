import json
from datetime import date
from typing import Generator

class Book:
    """Класс Book для работы с книгами

    Основное применение - сохранение информации о книгах в библиотеке
    
    Attributes:
        id (int): Идентификатор книги
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания книги
        status (str): Статус книги

    Methods:
        __init__(self, id, title, author, year, status): Инициализация объекта Book
        __str__(self): Возвращает строковое представление объекта Book

    Example:
        book = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "В наличии")

    """

    def __init__(self, id, title, author, year, status) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return f"ID: {self.id}, название книги: {self.title}, автор: {self.author}, год издания: {self.year}, статус: {self.status}"

class Library:
    """Класс Library для работы с библиотекой

    Основное применение - выполнение различных операций с книгами в библиотеке
    
    Attributes:
        file_name (str): Путь к файлу библиотеки
        books (list): Список книг в библиотеке

    Methods:
        __init__(self): Инициализация объекта Library
        load_books(self): Загрузка книг из файла
        save_books(self): Сохранение книг в файл
        add_book(self, title, author, year): Добавление книги в библиотеку
        delete_book(self, id): Удаление книги из библиотеки
        change_status(self, id): Изменение статуса книги
        display_books(self): Вывод всех книг в библиотеке
        search_book(self, data): Поиск книги в библиотеке
    """

    def __init__(self) -> None:
        self.file_name = "books/books.json"
        self.books: list[Book] | None = self.load_books()

    def load_books(self) -> list[Book] | None:
        """Метод для загрузки книг из файла
        
        Returns:
            list: Список книг, сохранённых в библиотеке
        
        Exeptions:
            FileNotFoundError: Если файл не найден, он создаётся с записью пустого списка Books
            json.JSONDecodeError: Если данные в файле некорректны, создаётся файл с записью пустого списка Books
        """

        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Book(book["id"], book["title"], book["author"], book["year"], book["status"]) for book in data["books"]]
            
        except FileNotFoundError:
            data = {"books": []}
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

        except json.JSONDecodeError:
            data = {"books": []}
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

    def save_books(self) -> None:
        """Метод для сохранения книг в файл

        Основное применение: сохранение книг в библиотеке
        """

        data: dict = {"books": [{"id": book.id, "title": book.title, "author": book.author, "year": book.year, "status": book.status} 
                          for book in self.books]}

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


    def add_book(self, title: str, author: str, year: str) -> str:
        """Метод для добавления книги в библиотеку

        Основное применение: добавление книги в библиотеку
        
        Args:
            title (str): Название книги
            author (str): Автор книги
            year (int): Год издания книги

        Returns:
            str: Сообщение о результате добавления книги

        Exeptions:
            ValueError: Если год издания некорректен
            TypeError: Если id последнего элемента некорректен, возникает при пустой библиотеке
            IndexError: Если id последнего элемента некорректен, возникает при пустой библиотеке
        """

        # загрузка списка книг
        self.load_books()

        try:
            year = int(year)
            if year < 1 or year > date.today().year:
                raise ValueError
        except ValueError:
            return "\nНекорректно введен год издания. Год должен быть числом не больше текущего года"

        try:
            last_id = self.books[-1].id
        except IndexError:
            last_id = 0
        except TypeError:
            last_id = 0

        data = Book(last_id + 1, title, author, year, "в наличии")

        try:
            self.books.append(data)
        except AttributeError:
            self.books = []
            self.books.append(data)
        
        #сохранение изменений
        self.save_books()

        return f"\nКнига {author} - {title} с годом издания {year} добавлена"
    
    def delete_book(self, id: str) -> str: 
        """Метод для удаления книги из библиотеки

        Основное применение: удаление книги из библиотеки
        
        Args:
            id (int): ID книги

        Returns:
            str: Сообщение о результате удаления книги или сообщение о том, что книга с указанным ID не была найдена

        Exeptions:
            TypeError: Если библиотека пуста
        """

        try:
            if self.books != []:

                for book in self.books:
                    if book.id == id:

                        self.books.remove(book)
                        self.save_books()

                        return f"\nКнига {book.author} - {book.title} удалена\n"

                return "\nКнига не найдена"
            
            else:
                return "\nБиблиотека пуста"

        except TypeError:
            return "\nБиблиотека пуста"
        

    def search_book(self, data: str) -> str:
        """Метод для поиска книги в библиотеке

        Основное применение: поиск книги в библиотеке
        
        Args:
            data (str): Данные для поиска: название книги, автор книги или год издания

        Returns:
            str: Сообщение о результате поиска с ID книги, названием, автором и годом издания
            или сообщение о том, что книга не была найдена

        Exeptions:
            TypeError: Если библиотека пуста
        """
        try:
            if self.books != []:

                found_books = list(filter(lambda book: data in (book.title, book.author, str(book.year)), self.books))
                if found_books: 
                    return "\n".join(f"ID: {book.id}, название: {book.title}, автор: {book.author}, год издания: {book.year}, статус: {book.status}" for book in found_books)
                else:
                    return "\nКнига не найдена"
                
            else: 
                return "\nБиблиотека пуста"

        except TypeError:
            return "\nБиблиотека пуста"
        
    def display_books(self) -> Generator:
        """Метод для отображения всех книг в библиотеке

        Основное применение: отображение всех книг в библиотеке

        Returns:
            str: Сообщение с информацией о всех книгах в библиотеке или сообщение о том, что библиотека пуста

        Exeptions:
            TypeError: Если библиотека пуста
        """

        try:
            if self.books != []:

                for book in self.books:
                    yield (f"ID: {book.id}, название книги: {book.title}, автор: {book.author}, год издания: {book.year}, статус: {book.status}")

            else:
                yield "\nБиблиотека пуста"

        except TypeError:    
            yield "\nБиблиотека пуста"
        
    def change_status(self, id: str) -> str:
        """Метод для изменения статуса книги в библиотеке

        Основное применение: изменение статуса книги в библиотеке по указанному ID
        
        Args:
            id (int): ID книги

        Returns:
            str: Сообщение о результате изменения статуса книги или сообщение о том, что книга не была найдена. 
            Если статус книги "в наличии", он будет изменен на "выдана". Если статус книги "выдана", он будет изменен на "в наличии"

        Exeptions:
            TypeError: Если библиотека пуста
        """

        try:
            if self.books != []:
                try:
                    for book in self.books:
                        if book.id == id:

                            if book.status == "в наличии":
                                input(f"\nКнига {book.title} в наличии. Нажмите Enter, чтобы выдать книгу")
                                book.status = "выдана"
                            else:
                                input(f"\nКнига {book.title} была выдана. Нажмите Enter, чтобы вернуть книгу в библиотеку")
                                book.status = "в наличии"

                            self.save_books()
                            return f"\nСтатус изменен. Книга {book.title} {book.status}"
                    raise ValueError("\nКнига не найдена")

                except ValueError:
                    return "\nКнига не найдена"
            else:
                return "\nБиблиотека пуста"

        except TypeError:       
            return "\nБиблиотека пуста"

#создание объекта класса Library
book = Library()