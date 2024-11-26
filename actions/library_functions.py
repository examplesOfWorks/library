import json
from datetime import date

class Book:
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, название книги: {self.title}, автор: {self.author}, год издания: {self.year}, статус: {self.status}"

class Library:
    def __init__(self):
        self.file_name = "library/books.json"
        self.books = self.load_books()

    def load_books(self):
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

    def save_books(self):
        data = {"books": [{"id": book.id, "title": book.title, "author": book.author, "year": book.year, "status": book.status} 
                          for book in self.books]}

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


    def add_book(self, title, author, year):

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
        
        self.save_books()

        return f"\nКнига {author} - {title} с годом издания {year} добавлена"
    

    def delete_book(self, id): 
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
        

    def search_book(self, data):
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
        
    def display_books(self):

        try:
            if self.books != []:

                for book in self.books:
                    yield (f"ID: {book.id}, название книги: {book.title}, автор: {book.author}, год издания: {book.year}, статус: {book.status}")

            else:
                yield "\nБиблиотека пуста"

        except TypeError:    
            yield "\nБиблиотека пуста"
        
    def change_status(self,id):

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
    
book = Library()


# print(book.add_book("title1", "author1", "2019"))
# print(book.add_book("title2", "author2", "2009"))
# print(book.add_book("title3", "author3", "2020"))

# print(book.delete_book(5))

# print(book.search_book("2011"))

# for b in book.display_books():
#     print(b)

# print(book.change_status(3))





