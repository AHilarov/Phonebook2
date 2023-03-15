import processor
import view
import variable

print()
print(f'{variable.start_prog}\n {60 * "_"}')
def start():

    while True:

        choice = view.print_menu()
        match choice:
            case 1:                
                view.print_phonebook(processor.open_file())
            case 2:
                processor.new_contact()
            case 3:
                processor.change_contact()
            case 4:
                processor.find_contact()                
            case 5:
                processor.delete_contact()
            case 6:
                # Если пользователь вводит 6, то цикл останавливается и программа завершается
                print(variable.exit)
                break
                