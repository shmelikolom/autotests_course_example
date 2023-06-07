# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
from contextlib import contextmanager


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@contextmanager
def does_not_raise():
    """Контекстный менеджер."""
    yield


@pytest.mark.parametrize('a, result, expectation', [pytest.param((21, 0, 1), None,
                                                    pytest.raises(ZeroDivisionError), marks=pytest.mark.smoke),
                                                    pytest.param((0, 21, 1), 0,
                                                    does_not_raise(), marks=pytest.mark.acceptance),
                                                    pytest.param(('a', 3, 7), None,
                                                    pytest.raises(TypeError), marks=pytest.mark.acceptance),
                                                    pytest.param((210, 7, 5), 6,
                                                    does_not_raise(), marks=pytest.mark.smoke),
                                                    pytest.param((210.1, 7.2, 6.1), 4.783697632058288,
                                                    does_not_raise(), marks=pytest.mark.skip)])
def test_division_float(a, result, expectation):
    """Проверка функции all_division"""
    with expectation:
        assert all_division(*a) == result

