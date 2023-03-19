import processor
import view
import variable
import sys, os
clear = lambda: os.system('cls')


def start():
    clear ()
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
                print(variable.delete_contacts)
                processor.delete_contact()
            case 6:
                print("Пока")
                break
                