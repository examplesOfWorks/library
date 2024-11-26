from time import sleep
from actions.menu_actions import *

def menu_run() -> None:
    """Метод для отображения меню и перехода к доступным в нём действиям

    Основное применение: запуск меню для работы с библиотекой
    
    Returns:
        None

    Exeptions:
        Exception: Если возникли какие-либо ошибки
    """

    menu_str = """
              МЕНЮ
        Выберите действие:
        1) Добавить книгу
        2) Удалить книгу
        3) Поиск книги
        4) Показать все книги
        5) Изменить статус книги
        0) Выход (или Ctrl+C)
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
            print("\nБудем рады видеть вас в библиотеке снова!")
            break

        # запуск действия, соответствующего выбору
        try:
            if choice == "1":
                go_1()
            elif choice == "2":
                go_2()
            elif choice == "3":
                go_3()
            elif choice == "4":
                print("\nСписок всех книг:")
                go_4()
            elif choice == "5":
                go_5()
            else:
                menu_print = False
                print("\nЭтого пункта меню не существует")
                continue

            input("\nНажмите Enter для продолжения...")
            menu_print = True

        except Exception as e:
            print("\nПроизошла ошибка:", e)
            sleep(3)
            input("\nНажмите Enter для продолжения...")
            continue




