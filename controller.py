import model
import text
import view


def search_note():
    word = view.input_request(text.input_search_word)
    result = model.find_note(word)
    view.show_notes(result, text.not_find(word))
    if result:
        return True
    

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.load_successful)
            case 2:
                model.save_file()
                view.print_message(text.save_successful)
            case 3:
                view.show_notes(model.book, text.empty_book_error)
            case 4:
                new_note = view.input_note(text.input_note)
                model.add_note(new_note)
                view.print_message(text.note_action(new_note[0], text.operation[0]))
            case 5:
                search_note()
            case 6:
                if search_note():
                    c_id = int(view.input_request(text.input_edit_note_id))
                    new_note = view.input_note(text.input_edit_note)
                    date = model.edit_note(c_id, new_note)
                    view.print_message(text.note_action(date, text.operation[1]))
            case 7:
                if search_note():
                    c_id = int(view.input_request(text.input_del_note_id))
                    name = model.delete_note(c_id)
                    view.print_message(text.contact_action(name, text.operation[2]))
            case 8:
                if model.original_book != model.phone_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        model.save_file()
                        view.print_message(text.save_successful)
                view.print_message(text.exit_program)
                break


