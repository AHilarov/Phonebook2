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

