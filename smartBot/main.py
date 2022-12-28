from smartBot.utils import change_input
from smartBot.address_book_classes import contacts_dict


def main():
    """
    Отримуємо ввід від користувача
    і відправляємо його в середину застосунку на обробку.
    :return:
    """
    try:
        while True:
            """
            Просимо користувача ввести команду для нашого бота
            Також тут же вимикаємо бота якщо було введено відповідну команду
            """

            user_input = input('Enter command for bot: ')
            result = change_input(user_input)
            print(result)
            if result == 'good bye':
                break
    finally:
        contacts_dict.save_contacts_to_file()


if __name__ == '__main__':
    main()
