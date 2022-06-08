from typing import Tuple, List

import pytest

from lns import load_numbers_sorted


@pytest.fixture
def txt(tmpdir) -> str:
    tmpfile = tmpdir.join('numbers.txt')

    with tmpfile.open('w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield str(tmpfile)

    tmpfile.remove()


@pytest.fixture
def txt_and_list(txt) -> Tuple[str, List[int]]:
    yield txt, [1, 2, 3, 4, 5]


def test_load_numbers_sorted(txt_and_list):
    assert load_numbers_sorted(txt_and_list[0]) == txt_and_list[1]
