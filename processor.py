
def find_contact():
    with open (r'phonebook.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        contact = input("Задайте имя или фамилию контакта для поиска: ")
        line_target = -1
        for line in data:
            if contact in line:
                print(contact, "существует в справочнике." )
                line_target = line
                print("Полная запись контакта: ", line)
        if line_target == -1:
            print("Такого контакта нет.")


# Первая версия - без задания изменяемой строки
def change_contact():
    with open(r'phonebook.txt', 'r', encoding="utf8") as file:
        data = file.read()
        print("Вот все записи справочника: \n")
        print(data, "\n")
        search_text = input("Введите запись, которую Вы хотете заменить: ")
        replace_text = input("На что вы хотите заменить: ")
        data = data.replace(search_text, replace_text)
    with open(r'phonebook.txt', 'w', encoding="utf8") as file:
        file.write(data)
    print("Изменения внесены.")
    

# Вторая версия - с заданием изменяемой строки
# def change_contact():
#     with open(r'phonebook.txt', 'r', encoding="utf8") as file:
#         data = file.readlines()
#         print("Вот все записи справочника: \n")
#         for i, line in enumerate(data, 1):
#             print(f'{i} : {line}')
#         print(type(data))
#         data = ''.join(str(x) for x in data)
#         target_line = input("Введите номер строки, в которую Вы хотете внести изменения: ")
#         search_text = input("Введите запись, которую Вы хотете заменить: ")
#         replace_text = input("На что вы хотите заменить: ")
#         for line in data:
#             if line == target_line:
#                 data = data.replace(search_text, replace_text)
#     with open(r'phonebook.txt', 'w', encoding="utf8") as file:
#         file.write(data)
#     print("Изменения внесены.")


def delete_contact():
    with open(r'phonebook.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        print(type(data))
        print(data)
        contact = input("Задайте имя или фамилию контакта для удаления: ")
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
    

def close_file():
    exit()

