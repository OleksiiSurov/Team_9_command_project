from commands import (hello_func, exit_func, add_func, change_phone_func, show_func, search_func, del_phone_func,
                      del_func, birthday_func, next_birthday_func)

COMMANDS_DICT = {
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
    'days to birthday': next_birthday_func
}