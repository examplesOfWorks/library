# Название
Система управления библиотекой
# Краткое описание.
Консольное приложение для управления библиотекой книг
# Основные возможности.
Добавление, удаление, поиск отдельной книги, отображение всего списка книг, а также изменение статуса книги с «в наличии» на «выдана» и наоборот.
Хранение данных реализовано в json формате. Обработаны основные ошибки и исключения. Функции написаны для каждой операции (добавление, удаление, поиск, отображение, изменение статуса). При написании проекта сторонние библиотеки не использовались.
В коде содержится аннотирование функций и переменных. Есть документации основным блокам кода: классам, функциям, пакетам. Использован объектно-ориентированный подход. 
# Инструкция по запуску.
Необходимо клонировать репозиторий командой
``` git clone https://github.com/examplesOfWorks/library.git ```
Далее перейти в папку library
В папке library запустить терминал и ввести команду 
``` python -m openlib ```
Откроется меню с возможными действиями. Для перехода к нужному пункту, необходимо написать его порядковый номер и нажать Enter.
# Подробное описание функционала.
Проект состоит из двух пакетов. В «actions» находятся два файла «library_functions» и «menu_actions». Пакет actions помогает создать текстовый интерфейс консольного приложения для управления библиотекой книг.
Данные хранятся в папке books в файле books.json. При отсутствии файла, при запуске библиотеки он создаётся, туда записывается список books, куда будут сохраняться все книги.
Каждая книга содержит следующие поля:
- id (уникальный идентификатор, генерируется автоматически)
- title (название книги)
- author (автор книги)
- year (год издания)
- status (статус книги: “в наличии”, “выдана”)
## Запуск приложения
Чтобы запуск приложения осуществлялся через команду ``` python -m openlib ```, был создан файл __main__.py. Он служит точкой входа в проект, запуская меню приложения через вызов функции menu_run(). Она находится в файле main.py. Выводится список действий, выбор которых вызывает соответствующую функцию. При выборе пункта 0 или нажатии Ctrl+C, пользователь выходит из приложения.
## Логика работы меню
Переход к функциям меню осуществляется в файле menu_actions.py. Каждой операции из меню соответствует своя функция.  
## Логика работы функций
Логика работы функций реализована в файле library_functions.py.
В файле library_functions.py. Объявляется класс Book, который ответственен за сохранение всей информации о каждой книге, и класс Library, каждому методу которого соответствует отдельная операция.
- добавление <br />
Метод add_book(). В функцию передаются название, автор, и год издания книги, последовательно введённые пользователем в консоль. Осуществляется проверка того, чтобы год был положительным числом не больше текущего года. Каждой введённой книге присваивается уникальный ID. Книги нумеруются по порядку, начиная с 1.
- удаление <br />
Метод delete_book(). В функцию передаётся ID, введённое пользователем в консоль. Если в базе данных есть книга с указанным ID, она удаляется. Выполняются проверки: ID должно быть числом, соответствовать определённой книге, а также библиотека не должна быть пустой.
- поиск книги <br />
Метод search_book(). В функцию передаются данные, введённые пользователем в консоль. Поиск можно осуществлять по названию, автору или году издания. Применяются функции filter и lambda для проверки условия, что указанные данные есть в записи о названии, авторе или годе издания. Выведутся строки о всех найденных книгах, если название, автор или год будут у них одинаковыми. Выполняются проверки: данные должны соответствовать определённой книге и библиотека не должна быть пустой. 
- отображение всех книг <br />
Метод display_books(). В функцию ничего не передаётся. Она просто выводит список всех книг с их ID, названием, автором, годом и статусом в указанном формате. Используется функция-генератор. Выполняется проверка: библиотека не должна быть пустой.
- изменение статуса <br />
Метод change_status().В функцию передаётся ID, введённое пользователем в консоль. Если книга с указанным ID в наличии (статус «в наличии»), при нажатии на Enter она выдается (её статус меняется на «выдана»). Таким же образом меняется статус с «выдана» на «в наличии», если книга уже была выдана. Выполняются проверки: книга должна быть найдена, ID должен быть числом, а также библиотека не должна быть пустой.
<br />
Сохранение изменений в базе данных происходит через метод save_books(). Функция вызывается тогда, когда это необходимо. Загрузка всех имеющихся в библиотеке книг происходит с помощью метода load_books().
