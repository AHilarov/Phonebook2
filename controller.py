import processor

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                processor.open_file()
            case 2:
                processor.save_file()
            case 3:                
                view.show_contacts(processor.get_contacts())
            case 4:
                processor.new_contact(processor.get_contacts())
            case 5:
                processor.change_contact()
            case 6:
                processor.find_contact()
                
            case 7:
                processor.delete_contact()
            case 8:
                pass
                break