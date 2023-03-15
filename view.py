from tabulate import tabulate
import variable
# интефейс взаимодействия с пользователем
# print_menu(): функция для вывода меню на экран пользователя
def print_menu():
    print('''\nГлавное меню:
    1. Показать контакты
    2. Создать контакт
    3. Изменить контакт
    4. Найти контакт
    5. Удалить контакт
    6. Выход
    ''')
    print(60 * "_")
    user_input = int(input(f'{variable.menu_selection}'))
    print()
    
    if 0 < user_input < 7:
        return user_input
    else:
        print_msg(variable.error)
        return print_menu()

# print_msg(msg): функция для вывода сообщения на экран пользователя
def print_msg(msg):
    print(60 * "_")
    print(msg)
    print(60 * "_")

# print_phonebook(): функция для вывода справочника
def print_phonebook(arr):
    print(60 * "_")
    print(19 * "_" + variable.open_book +  19 * "_" )
    print()
    print(tabulate(arr, headers=variable.first_line))
    print(60 * "_")