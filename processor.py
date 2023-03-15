from copy import deepcopy
import variable
import view

phone_book = []
new_phone_book = []
path = 'phonebook.txt'



#  Функция для вывода на экран нашего файла(без форматирования)
def open_first_phonebook():
    phonebook_lst = ''
    path = 'phonebook.txt'
    data = open('phonebook.txt', 'r', encoding='UTF-8')
    for line in data:
        phonebook_lst += line
    data.close()
    print(phonebook_lst)




# Функция для передачи списка из словарей для каждого контакта
def open_file():
    global phone_book
    global new_phone_book
    global path
    go_back = input("Если хотите продолжить введите 1\nЕсли хотите вернуться в главное меню то 0: ")
    if go_back == '1':
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
    else:
        print()




# Функция для сохранения(не пригодилась, но оставим здесь)
# def save_file():
#     file = input('Имя файла для сохранения (enter - имя файла для сохранения)')
#     if not file:
#         file = path
#     with open(path, 'w') as data:
#         data.writelines(' '.join(map(str, )))
#         data.write('\n')
            




# Функция для добавления новых контактов
def new_contact():
    global phone_book
    go_back = input("Если хотите продолжить введите 1\nЕсли хотите вернуться в главное меню то 0: ")
    if go_back == '1':
        a = input('Введите имя нового пользователя: ')
        b = input('Введите фамилию нового пользователя: ')
        c = input('Введите телефон нового пользователя: ')
        d = input('Введите комментарий нового пользователя: ')
        new_contact = f'{a};{b};{c};{d}'
        with open(path, 'a', encoding='UTF-8') as data:
            data.writelines('\n')
            data.writelines(new_contact)
        view.print_msg(variable.save_book)
    else:
        print()
  



# Функция для поиска контакта по фамилии
def find_contact():
    go_back = input("Если хотите продолжить введите 1\nЕсли хотите вернуться в главное меню то 0: ")
    if go_back == '1':
        with open ('phonebook.txt', 'r', encoding='UTF-8') as data:
            contact = input('Пожалуйста, задайте фамилию адресата для поиска: ')
            lines = data.readlines()
            found = False
            for line in lines:
                if contact in line:
                    print("Вот контакт, который Вы искали: ", end=' ')
                    print(line)
                    found = True
                    break
            if found == False:
                print("Контакта с такой фамилией нет")
    else:
        print()
    



# Функция для замены данных о контакте
def change_contact():
    go_back = input("Если хотите продолжить введите 1\nЕсли хотите вернуться в главное меню то 0: ")
    if go_back == '1':
        print("Вот все записи справочника: ")
        print()
        open_first_phonebook()
        print()
        text1 = input("Введите строку котрую будете менять: ")
        text2 = input("На что меняем: ")
        
        with open ('phonebook.txt', 'r', encoding='UTF-8') as f:
            old_data = f.read()
        new_data = old_data.replace(text1, text2)
        with open ('phonebook.txt', 'w', encoding='UTF-8') as f:
            f.write(new_data)
        view.print_msg(variable.save_book)
    else:
        print()



# Функция для удаления контакта
def delete_contact():
    go_back = input("Если хотите продолжить введите 1\nЕсли хотите вернуться в главное меню то 0: ")
    if go_back == '1':
        print("Вот все записи справочника: ")
        print()
        open_first_phonebook()
        print()
        line_del = input("Введите строку для удаления: ")

        try:
            with open('phonebook.txt', 'r', encoding='UTF-8') as fr:
                lines = fr.readlines()
    
                with open('phonebook.txt', 'w', encoding='UTF-8') as fw:
                    for line in lines:
                        if line.strip('\n') != line_del:
                            fw.write(line)
            view.print_msg("Контакт удален")
        except:
            print(variable.error)
    else:
        print()