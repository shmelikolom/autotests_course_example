
import datetime
import pytest


@pytest.fixture(scope='class')
def time_class():
    print(datetime.datetime.now().strftime("%d.%m %H:%M:%S\n"))
    yield
    print(datetime.datetime.now().strftime("%d.%m %H:%M:%S\n"))


@pytest.fixture
def time_test():
    time = datetime.datetime.now()
    yield
    print(datetime.datetime.now() - time)



