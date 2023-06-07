# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_division_zero():
    """Проверка деления на ноль"""
    with pytest.raises(ZeroDivisionError):
        all_division(21, 0, 1)


@pytest.mark.smoke
def test_zero_division():
    """Проверка деления нуля """
    assert all_division(0, 21, 1) == 0


@pytest.mark.acceptance
def test_division_str():
    """Проверка деления не возможности деления строки"""
    with pytest.raises(TypeError):
        all_division('a', 3, 7)


@pytest.mark.acceptance
def test_division_int():
    """Проверка целочисленого деления"""
    assert all_division(210, 7, 5) == 6


@pytest.mark.acceptance
def test_division_float():
    """Проверка дления не целых чисел"""
    assert all_division(210.1, 7.2, 6.1) == 4.783697632058288



