# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import time


class TestCRUD:

    def test_1(self, time_class):
        time.sleep(3)

    def test_2(self, time_class):
        time.sleep(3)

    def test_delete(self, time_class, time_test):
        time.sleep(3)
