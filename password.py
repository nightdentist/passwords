password = input('Введите пароль: ')


score = 0


def is_very_long(password):
    if len(password) >= 12:
        return True


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_letters(password):
    return any(character.isalpha() for character in password)


def has_upper_letters(password):
    return any(character.isupper() for character in password)


def has_lower_letters(password):
    return any(character.islower() for character in password)


functions = [is_very_long(password),
             has_digit(password),
             has_letters(password),
             has_upper_letters(password),
             has_lower_letters(password)]

for i in functions:
    if i == True:
        score = score + 2

print("Рейтинг пароля: " + str(score))
