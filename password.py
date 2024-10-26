import urwid


def is_very_long(password):
    if len(password) >= 12:
        return


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_letters(password):
    return any(character.isalpha() for character in password)


def has_upper_letters(password):
    return any(character.isupper() for character in password)


def has_lower_letters(password):
    return any(character.islower() for character in password)


def has_symbols(password):
    return any(character in ".,:;!_*-+@`$()/#¤%&)" for character in password)


def on_ask_change(edit, new_edit_text):
    password = new_edit_text
    score = 0
    functions = [
        is_very_long(password),
        has_digit(password),
        has_letters(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
        ]
    for i in functions:
        if i:
            score = score + 2
    reply.set_text("Рейтинг этого пароля: %s" % str(score))


ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()
