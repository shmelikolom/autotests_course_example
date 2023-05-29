# Напишите класс Trigon, для инициализации передаётся неизвестное кол-во атрибутов

# В классе при инициализации происходит проверка на корректность переданных данных и генерируются следующие исключения:

# 1) Если хотя бы одна сторона передана не числом,
# то падаем с TypeError и текстом 'Стороны должны быть числами'

# 2) Если хотя бы одна сторона передана нулем или отрицательным числом,
# то падаем с ValueError и текстом 'Стороны должны быть положительными'

# 3) Если не соблюдается неравество треугольника,
# то Exception и текст "Не треугольник"

# 4) Если передано не 3 аргумента, то IndexError "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

import unittest  # Не удалять


class Trigon:
    """Класс треугольника.

    Атрибуты
    --------
    triangle: tuple
        Кортеж со сторонами треугольника
    """
    def __init__(self, *triangle):
        """Устанавливает все необходимые атрибуты для объекта Trigon

        Параметры
        --------
        triangle: tuple
        Кортеж со сторонами треугольника

        Проверки
        --------
        Передано 3 стороны, иначе бросается исключение IndexError
            "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

        Все стороны являются числами, иначе бросается исключение TypeError 'Стороны должны быть числами'

        Стороны больше нуля, иначе бросается исключение ValueError 'Стороны должны быть положительными'

        Соблюдается неравество треугольника, иначе бросается исключение Exception "Не треугольник"
        """

        if len(triangle) != 3:  # Проврека что передали 3 стороны треугольника
            raise IndexError(f"Передано {len(triangle)} аргументов, а ожидается 3")
        try:
            if min(triangle) <= 0:  # Проверяем что стороны треугольника больше 0
                raise ValueError('Стороны должны быть положительными')
            elif sum(triangle) < 2 * max(triangle):  # Проверяем что с такими сторонами треугольник существует
                raise Exception("Не треугольник")
        except TypeError:
            raise TypeError('Стороны должны быть числами')
        self.triangle = triangle
# Здесь пишем код

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, '7', 5), (-3, 7, 5), (2, 5, 2), (3, 4, 5, 6), (3, 4), (3, 4, 5)]

        test_data = [('Стороны должны быть числами', 'TypeError'),
                     ('Стороны должны быть положительными', 'ValueError'),
                     ("Не треугольник", 'Exception'),
                     ("Передано 4 аргументов, а ожидается 3", 'IndexError'),
                     ("Передано 2 аргументов, а ожидается 3", 'IndexError'),
                     0]
        for i, d in enumerate(data):
            try:
                Trigon(*data[i])
            except Exception as e:
                assert e.args[0] == test_data[i][0], 'Исключение имеет неправильный текст'
                assert type(e).__name__ == test_data[i][1], 'У исключения неправильный тип'

        print('Всё ок')


if __name__ == '__main__':
    unittest.main()
