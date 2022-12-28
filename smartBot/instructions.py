from smartBot.commands import (hello_func, exit_func, add_func, change_phone_func, show_func, search_func, del_phone_func,
                               del_func, birthday_func, next_birthday_func, add_notes_func, who_have_birthdays_func,
                               add_email_func, add_address_func, change_notes_func, delete_notes_func, search_notes_func, \
                               help_func)

COMMANDS_DICT = {
    'address': add_address_func,
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change phone': change_phone_func,
    'show all': show_func,
    'phone': search_func,
    'delete phone': del_phone_func,
    'delete': del_func,
    'birthday': birthday_func,
    'days to birthday': next_birthday_func,
    'notes': add_notes_func,
    'change notes': change_notes_func,
    'remove notes': delete_notes_func,
    'search': search_notes_func,
    'who have birthdays': who_have_birthdays_func,
    'email': add_email_func,
    'help': help_func
}
