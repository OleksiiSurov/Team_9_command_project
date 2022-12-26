def input_error(function):
    """
    Створюємо декоратор для обробки помилок, котрі можуть виникнути через
    ввід користувача.
    :param function: Функція вводу від користувача.
    :return: Або роботу функції або текст з помилкою, для повторного вводу.
    """

    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'

    return wrapper
