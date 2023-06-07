# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    # Здесь пишем код
    mark = next(request.node.iter_markers())
    print(mark.args)
    pass
