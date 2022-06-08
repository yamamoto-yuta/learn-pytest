import os

import pytest

from lns import load_numbers_sorted


@pytest.fixture
def txt() -> str:
    # 前処理
    with open('numbers.txt', 'w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    # テストに渡す値
    yield 'numbers.txt'

    # 後処理
    os.remove('numbers.txt')


def test_load_numbers_sorted(txt):
    assert load_numbers_sorted(txt) == [1, 2, 3, 4, 5]
