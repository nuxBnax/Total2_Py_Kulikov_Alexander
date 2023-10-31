menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать все заметки',
        'Создать заметку',
        'Найти заметку',
        'Изменить заметку',
        'Удалить заметку',
        'Выход',]

input_menu = 'Выберите пункт меню: '

input_menu_error = f'Ввести нужно ЧИСЛО ( от 1 до  {len(menu) - 1})'

load_successful = 'Файл с заметками загружен успешно!'
save_successful = 'Файл с заметками сохранен успешно!'

empty_book_error = 'Файл с заметками пуст или не открыт'

input_note = ['Введите Заголовок заметки: ',
                 'Введите Текст(содержимое заметки): ']

input_edit_note = ['Введите НОВОЕ название Заголовка заметки или ENTER, чтобы оставить без изменений: ',
                      'Введите НОВЫЙ Текст(содержимое заметки) или ENTER, чтобы оставить без изменений: ']

input_search_word = 'Введите искомую дату в следующем формате 12.12.2323: '
 
input_edit_note_id = 'Введите ID заметки, которую хотите изменить: '
input_del_note_id = 'Введите ID заметки, которую хотите удалить: '

operation = ['создана', 'изменена', 'удалена']

confirm_changes = 'У вас есть несохраненные изменения! Сохранить? (y/n)'
exit_program = 'До свидания! До новых встреч!'

def note_action(name: str, action: str) -> str:
    return f'Заметка {name} успешно {action}!'


def not_find(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'