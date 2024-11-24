from time import sleep
from menu_actions import *

def menu_run() -> None:

    menu_str = """
        Выберите действие:
        1) Добавить книгу
        2) Удалить книгу
        3) Поиск книги
        4) Показать все книги
        5) Изменить статус книги
        0) Выход
        menu - меню
    """

    menu_print = True

    while True:

        # печать меню из возможных действий
        if menu_print:
            print(menu_str)

        # выбор действия
        choice = input("Выберите пункт меню: ")

        # при выборе выхода выходим из программы
        if choice == "0":
            break

        # запуск действия, соответствующего выбору
        try:
            if choice == "1":
                go_1()
            elif choice == "2":
                go_2()
            elif choice == "3":
                print("Результаты поиска:")
                go_3()
            elif choice == "4":
                print("Список всех книг:")
                go_4()
            elif choice == "5":
                go_5()
            elif choice == "help":
                print(menu_str)
            else:
                print("Этого пункта меню не существует")
                continue

            if choice != "menu":
                menu_print = False

            input("Нажмите Enter для продолжения...")

        except Exception as e:
            print("Произошла ошибка:", e)
            sleep(3)
            input("Нажмите Enter для продолжения...")
            continue
menu_run()