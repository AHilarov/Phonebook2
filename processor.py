def open_file():
    dictionary = {}
    with open ('phonebook.txt', 'r') as data:
        for line in data:
            for i in range (len(line)):
                if data[i] == ';':
                    dictionary = {'name': data[:i]}

def save_file():
    file = input('Имя файла для сохранения (enter - имя файла для сохранения)')
    if not file:
        file = 'phonebook'
    with open('phonebook.txt', 'w') as data:
        data.writelines(' '.join(map(str, )))
        data.write('\n')
    


def get_contacts():
    pass

def new_contact(dictionary, name, surname, number, comment):
    pass


def find_file():
    with open ('phonebook.txt', 'r') as data:
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
    pass

def change_file():
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
    pass

def delete_file():
    f = open('phonebook.txt', 'r')
    lines = f.readlines()
    f.close()
    f = open('phonebook.txt', 'w')
    line_del = int(input("Введите номер строки для удаления: "))
    for line in lines:
        if line != line_del:
            f.write(line)
    f.close()
    pass

def finish_file():
    quit()

