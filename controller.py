import processor
import view


def start():

    while True:

        choice = view.print_menu()
        match choice:
            case 1:
                processor.open_file()
            case 2:
                processor.save_file()
            case 3:                
                view.print_phonebook(processor.open_file())
            case 4:
                processor.new_contact()
            case 5:
                processor.change_contact()
            case 6:
                processor.find_contact()                
            case 7:
                processor.delete_contact()
            case 8:
                processor.finish_file()
                