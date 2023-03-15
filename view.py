from tabulate import tabulate
import variable
# интефейс взаимодействия с пользователем
# print_menu(): функция для вывода меню на экран пользователя
def print_menu():
    print('''\nГлавное меню:
    1. Отрыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход
    ''')

# print_msg(msg): функция для вывода сообщения на экран пользователя
def print_msg(msg):
    print(50 * "_")
    print(msg)
    print(50 * "_")

# print_phonebook(): функция для вывода справочника
def print_phonebook(arr):
    print(tabulate(arr, headers=variable.first_line))