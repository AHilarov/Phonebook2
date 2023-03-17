import processor
import view


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
                print("Пока")
                break
                