from copy import deepcopy
import variable

phone_book = []
new_phone_book = []
path = 'phonebook.txt'


def open_file():
    global phone_book
    global new_phone_book
    global path
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            new = line.strip().split(';')
            new_contact = {}
            new_contact['name'] = new[0]
            new_contact['surname'] = new[1]
            new_contact['phone'] = new[2]
            new_contact['comment'] = new[3]
            phone_book.append(new_contact)
    new_phone_book = deepcopy(phone_book)
    return new_phone_book


def save_file():
    file = input('Имя файла для сохранения (enter - имя файла для сохранения)')
    if not file:
        file = path
    with open(path, 'w') as data:
        data.writelines(' '.join(map(str, )))
        data.write('\n')
            
def new_contact():
    global phone_book
    name = input('Введите имя нового пользователя: ')
    surname = input('Введите фамилию нового пользователя: ')
    phone = input('Введите телефон нового пользователя: ')
    comment = input('Введите комментарий нового пользователя: ')
    new_contact = f'{name};{surname};{phone};{comment}'
    with open(path, 'a', encoding='UTF-8') as data:
        data.writelines('\n')    
        data.writelines(new_contact)
    print(variable.added_contact)
  

def find_contact():
    global phone_book
    print (phone_book)
    # print(f'''\nКак будем искать?
    # 1. Показать контакты
    # 2. Создать контакт
    # 3. Изменить контакт
    # 4. Найти контакт
    # 5. Удалить контакт
    # 6. Выход
    # \n{variable.menu_selection}''', end='')
    # with open ('phonebook.txt', 'r') as data:
    #     contact = input('Пожалуйста, задайте фамилию адресата для поиска: ')
    #     lines = data.readlines()
    #     found = False
    #     for line in lines:
    #         if contact in line:
    #             print("Вот контакт, который Вы искали: ", end=' ')
    #             print(line)
    #             found = True
    #             break
    #     if found == False:
    #         print("Контакта с такой фамилией нет")
    

def change_contact():
    fin = open('phonebook.txt', 'r')
    data = fin.read()
    print("Вот все записи справочника: ", end=' ')
    print(data)
    text_1 = str(input("Введите запись, которую Вы хотете заменить: ", end=' '))
    text_2 = str(input("На что вы хотите заменить: ", end=' '))
    data = data.replace(text_1, text_2)
    fin.close()
    fin = open('phonebook.txt', 'w')
    fin.write(data)
    fin.close
    

def delete_contact():
    f = open('phonebook.txt', 'r')
    lines = f.readlines()
    f.close()
    f = open('phonebook.txt', 'w')
    line_del = int(input("Введите номер строки для удаления: "))
    for line in lines:
        if line != line_del:
            f.write(line)
    f.close()
    

def finish_file():
    quit()

