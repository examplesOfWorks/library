from library_functions import *

def go_1() -> None:
    title: str = input("Введите название книги: ")
    author: str = input("Введите автора книги: ")
    year: str = str(input("Введите год издания книги: ")) 

    try:
        result = add_book(title, author, year)
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_2():
    id: str = input("Для удаления книги введите её ID: ")
    try:
        result = delete_book(int(id))
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_3():
    data = input("Для поиска книги введите её название, автора или год издания: ")
    try:
        result = search_book(data)
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_4():
    try:
        for book in display_books():
            print(book)
    except Exception as e:
        print(e)

def go_5():
    id = input("Для изменения статуса книги введите её ID: ")
    try:
        result = change_status(int(id))
        if result:
            print(result)
    except Exception as e:
        print(e)
