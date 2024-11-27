from actions.library_functions import *

def go_1() -> None:
    """Метод перехода к добавлению книги в библиотеку.
    
    Основное применение: добавление книги в библиотеку. Пользователь вводит название книги, автора и год издания. 
    Изменения сохраняются в библиотеку при помощи метода add_book.

    Returns:
        None

    Exeptions:
        Exception: Если возникли какие-либо ошибки в работе функции add_book
    """

    title: str = input("\nВведите название книги: ")
    author: str = input("Введите автора книги: ")
    year: str = str(input("Введите год издания книги: ")) 

    try:
        result: str = book.add_book(title, author, year)
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_2() -> None:
    """Метод для перехода к удалению книги из библиотеки.
    
    Основное применение: переход к удалению книги из библиотеки. Пользователь вводит ID книги. 
    Изменения сохраняются в библиотеку при помощи метода delete_book.

    Returns:
        None

    Exeptions:
        Exception: Если возникли какие-либо ошибки в работе функции delete_book
    """
    id: str = input("Для удаления книги введите её ID: ")
    try:
        result = book.delete_book(id)
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_3() -> None:
    """Метод для перехода к поиску книги в библиотеке.
    
    Основное применение: переход к поиску книги в библиотеке. Пользователь вводит название книги, автора или год издания. 
    Поиск происходит при помощи метода search_book.

    Returns:
        None

    Exeptions:
        Exception: Если возникли какие-либо ошибки в работе функции search_book
    """

    data: str = input("\nДля поиска книги введите её название, автора или год издания: ")
    print("\nРезультаты поиска:")
    try:
        result = book.search_book(data)
        if result:
            print(result)
    except Exception as e:
        print(e)

def go_4() -> None:
    """Метод для перехода к отображению всех книг в библиотеке.
    
    Основное применение: переход к отображению всех книг в библиотеке. Выводится список всех книг с их ID, названием, автором, годом издания и статусом. 
    Получение списка всех книг происходит при помощи метода display_books.

    Returns:
        None

    Exeptions:
        Exception: Если возникли какие-либо ошибки в работе функции display_books
    """

    try:
        for b in book.display_books():
            print(b)
    except Exception as e:
        print(e)

def go_5() -> None:
    """Метод для перехода к изменению статуса книги в библиотеке.
    
    Основное применение: переход к изменению статуса книги в библиотеке. Пользователь вводит ID книги. 
    Изменения сохраняются в библиотеку при помощи метода change_status.

    Returns:
        None

    Exeptions:
        Exception: Если возникли какие-либо ошибки в работе функции change_status
    """
    id: str = input("\nДля изменения статуса книги введите её ID: ")
    try:
        result: str = book.change_status(id)
        if result:
            print(result)
    except Exception as e:
        print(e)

