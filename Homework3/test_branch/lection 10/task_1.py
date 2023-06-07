# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    """Генератор имени.

     Возвращает  два слова из латинских букв от 1 до 15 символов, разделенных пробелами."""
    letters = string.ascii_lowercase
    while 1:
        name = ''.join(random.choice(letters) for i in range(random.randint(1, 15))) + ' '
        name += ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
        yield name


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Здесь пишем код
