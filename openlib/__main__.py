from openlib.main import menu_run

# Запуск библиотеки
if __name__ == "__main__":
    print("\nДобро пожаловать в библиотеку!")
    try:
        menu_run()
    except KeyboardInterrupt:
        print("\n\nБудем рады видеть вас в библиотеке снова!")
else:
    print("Запуск не удался")