import json
from datetime import date

def add_book(title, author, year):
    try:
        with open("library/books.json", 'r', encoding='utf-8') as file:
            all_books = json.load(file)
    except FileNotFoundError:
        all_books = {"books": []}

    try:
        year = int(year)
        if year < 1 or year > date.today().year:
            raise ValueError
    except ValueError:
        return "Некорректно введен год издания. Год должен быть числом не больше текущего года"

    try:
        last_id = all_books["books"][-1]["id"]
    except IndexError:
        last_id = 0

    data = {
        "id": last_id + 1,
        "title": title,
        "author": author,
        "year": year,
        "status": "в наличии"
    }

    all_books["books"].append(data)
    with open("library/books.json", 'w', encoding='utf-8') as file:
        json.dump(all_books, file, indent=4)
    return f"Книга {author} - {title} с годом издания {year}  добавлена"

# print(add_book("title1", "author1", "2024"))
# print(add_book("title2", "author2", "1998"))
# print(add_book("title3", "author3", "2004"))
# print(add_book("title4", "author4", "2021"))
# print(add_book("title5", "author5", "2022"))

def delete_book(id) -> None:
    try:

        with open("library/books.json", 'r', encoding='utf-8') as file:
            all_books = json.load(file)
        try:
            for book in all_books["books"]:
                if book["id"] == id:
                    all_books["books"].remove(book)
                    with open("library/books.json", 'w', encoding='utf-8') as file:
                        json.dump(all_books, file, indent=4)
                    return f"Книга {book["author"]} - {book["title"]} удалена"
            raise ValueError("Книга не найдена")

        except ValueError:
            return "Книга не найдена"
        
    except FileNotFoundError:
        return "Библиотека пуста, пожалуйста, добавьте хотя бы одну книгу"

# print(delete_book(1))
# print(delete_book(2))
# print(delete_book(3))
# print(delete_book(4))
# print(delete_book(5))


def search_book(data):
    try:
       
        with open("library/books.json", 'r', encoding='utf-8') as file:
            all_books = json.load(file)
        found_books = list(filter(lambda book: data in (book["title"], book["author"], str(book["year"])), all_books["books"]))
        if found_books:
            return "Найдено:\n" + "\n".join(f"ID: {book['id']}, название: {book["title"]}, автор: {book['author']}, год издания: {book['year']}, статус: {book['status']}" for book in found_books)
        else:
            return "Книга не найдена"

    except FileNotFoundError:
        return "Библиотека пуста, пожалуйста, добавьте хотя бы одну книгу"


# print(search_book("title4"))

def display_books():

    try:

        with open("library/books.json", 'r', encoding='utf-8') as file:
            all_books = json.load(file)["books"]
            if all_books != []:
                i = 0
                while i < len(all_books):
                    yield (f"ID: {all_books[i]['id']}, название книги: {all_books[i]['title']}, автор: {all_books[i]['author']}, год издания: {all_books[i]['year']}, статус: {all_books[i]['status']}")
                    i += 1    
            else:
                yield "Библиотека пуста"

    except FileNotFoundError:
        yield "Библиотека пуста, пожалуйста, добавьте хотя бы одну книгу"

# for book in display_books():
#     print(book)

def change_status(id):

    try:

        with open("library/books.json", 'r', encoding='utf-8') as file:
            all_books = json.load(file)

        try:
            for book in all_books["books"]:
                if book["id"] == id:
                    if book["status"] == "в наличии":
                        input(f"Книга {book['title']} в наличии. Нажмите Enter, чтобы выдать книгу")
                        book["status"] = "выдана"
                    else:
                        input(f"Книга {book['title']} была выдана. Нажмите Enter, чтобы вернуть книгу в библиотеку")
                        book["status"] = "в наличии"
                    with open("library/books.json", 'w', encoding='utf-8') as file:
                        json.dump(all_books, file, indent=4)
                    return f"Статус изменен. Книга {book['title']} {book['status']}"
            raise ValueError("Книга не найдена")

        except ValueError:
            return "Книга не найдена"
        
    except FileNotFoundError:
        return "Библиотека пуста, пожалуйста, добавьте хотя бы одну книгу"
    
# print(change_status(2))
