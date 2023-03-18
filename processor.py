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
    with open (path, 'r', encoding="utf8") as file:
        data = file.readlines()
        contact = input(variable.find_contacts)
        contacts_found = []
        line_target = -1
        for line in data:
            if contact in line:
                line_target = line
                contacts_found.append(line)     
        if line_target == -1:
            print(variable.no_contact)
    print(*contacts_found)


def change_contact():
    with open(path, 'r+', encoding="utf8") as file:
        data = file.readlines()
        contact = input(variable.find_contacts)
        contacts_found = []
        line_target = -1
        for line in data:
            if contact in line:
                line_target = line
                contacts_found.append(line)
        if line_target != -1:
            if len(contacts_found) > 1:
                print(variable.confirm_contacts)
                for i, line in enumerate(contacts_found, 1):
                    print(f'{i} : {line}')
                id_del = int(input(variable.change_contacts))
                line_change = contacts_found[id_del - 1]
            else:   
                line_change = line_target
                for i, line in enumerate(contacts_found, 1):
                    print(f'{i} : {line}')
            replace_data = input(variable.replace_data)
            file.seek(0)
            for line in data:
                if line == line_change:
                    file.write(f'{replace_data}\n')
                else:
                    file.write(line)
            print(variable.confirm_change)
        else:
            print(variable.no_contact)


def delete_contact():
    with open (path, 'r+', encoding="utf8") as file:
        data = file.readlines()
        contact = input(variable.find_contacts)
        contacts_found = []
        line_target = -1
        for line in data:
            if contact in line:
                line_target = line
                contacts_found.append(line)
        if line_target == -1:
            print(variable.no_contact)
        if len(contacts_found) > 1:
            print(variable.confirm_contacts)
            for i, line in enumerate(contacts_found, 1):
                print(f'{i} : {line}')
            id_del = int(input(variable.delete_contacts))
            line_del = contacts_found[id_del - 1]
        else:   
            line_del = line_target
        file.seek(0)
        for line in data:
            if line != line_del:
                file.write(line)
        file.truncate()
