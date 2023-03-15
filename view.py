# from tabulate import tabulate
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
    while True:
        try:
            user_input = int(input())
            if 0 < user_input < 9:
                return user_input
            else:
                print(variable.error)
        except:
            print(variable.error)

# print_msg(msg): функция для вывода сообщения на экран пользователя
def print_msg(msg):
    print(50 * "_")
    print(msg)
    print(50 * "_")

# print_phonebook(): функция для вывода справочника
def print_phonebook(arr):
    print(arr, headers=variable.first_line)