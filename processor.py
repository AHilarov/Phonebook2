from copy import deepcopy
import variable

path = 'phonebook.txt'

def check_file():
    with open (path, 'a', encoding='UTF-8') as file:
        return ' '
    
def open_file():
    phone_book = []
    new_phone_book = []
    count = 0
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            count += 1
            new = line.strip().split(';')
            new_contact = {}
            new_contact['id'] = count
            new_contact['name'] = new[0]
            new_contact['surname'] = new[1]
            new_contact['phone'] = new[2]
            new_contact['comment'] = new[3]
            phone_book.append(new_contact)
    new_phone_book = deepcopy(phone_book)
    if count >= 1:
        return new_phone_book
    else:
        print(variable.empty_dir)
        return ' '
   
      
def new_contact():
    phone_book = []
    name = input('Введите имя нового пользователя: ')
    surname = input('Введите фамилию нового пользователя: ')
    phone = input('Введите телефон нового пользователя: ')
    comment = input('Введите комментарий нового пользователя: ')
    new_contact = f'{name};{surname};{phone};{comment}'
    with open(path, 'a', encoding='UTF-8') as data:
        data.writelines('\n')    
        data.writelines(new_contact)
    print(variable.added_contact)
      
def find_contact() -> list:
    with open (r'phonebook.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        contact = input(variable.find_contacts)
        line_target = -1
        for line in data:
            if contact in line:
                print(contact, "существует в справочнике." )
                line_target = line
                print("Полная запись контакта: ", line)
        if line_target == -1:
            print(variable.no_contact)
    
# Первая версия - без задания изменяемой строки
# def change_contact():
#     with open(r'phonebook.txt', 'r', encoding="utf8") as file:
#         data = file.read()
#         print("Вот все записи справочника: \n")
#         print(data, "\n")
#         search_text = input("Введите запись, которую Вы хотете заменить: ")
#         replace_text = input("На что вы хотите заменить: ")
#         data = data.replace(search_text, replace_text)
#     with open(r'phonebook.txt', 'w', encoding="utf8") as file:
#         file.write(data)
#     print("Изменения внесены.")
    

# Вторая версия - с заданием изменяемой строки
def change_contact():
    with open(r'phonebook.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        print("Вот все записи справочника: \n")
        for i, line in enumerate(data, 1):
            print(f'{i} : {line}')
        data = ''.join(str(x) for x in data)
        target_line = input("Введите номер строки, в которую Вы хотете внести изменения: ")
        search_text = input("Введите запись, которую Вы хотете заменить: ")
        replace_text = input("На что вы хотите заменить: ")
        for line in data:
            if line == target_line:
                data = data.replace(search_text, replace_text)
    with open(r'phonebook.txt', 'w', encoding="utf8") as file:
        file.write(data)
    print("Изменения внесены.")

def delete_contact():
    with open(r'phonebook.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        contact = input(variable.delete_contacts).lower()
        line_del = -1
        for line in data:
            if contact in line:
                print(contact, "существует в справочнике. Запись будет удалена." )
                line_del = line
        if line_del == -1:
            print("Такого контакта нет. Справочник не будет изменен.")
    with open(r'phonebook.txt', 'w', encoding="utf8") as file:
        for line in data:
            if line != line_del:
                file.write(line)
        data = ''.join(str(x) for x in data)
    

