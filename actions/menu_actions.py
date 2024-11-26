from actions.library_functions import *

def go_1() -> None:
    title: str = input("\nВведите название книги: ")
    author: str = input("Введите автора книги: ")
    year: str = str(input("Введите год издания книги: ")) 

    try:
        result = book.add_book(title, author, year)
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_2():
    id: str = input("Для удаления книги введите её ID: ")
    try:
        result = book.delete_book(int(id))
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_3():
    data = input("\nДля поиска книги введите её название, автора или год издания: ")
    print("\nРезультаты поиска:")
    try:
        result = book.search_book(data)
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_4():
    try:
        for b in book.display_books():
            print(b)
    except Exception as e:
        print(e)

def go_5():
    id = input("\nДля изменения статуса книги введите её ID: ")
    try:
        result = book.change_status(int(id))
        if result:
            print(result)
    except Exception as e:
        print(e)

