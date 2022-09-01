import enum
import itertools
from re import M
from typing import Iterable
import unittest


class C(enum.IntFlag):
    WHITE = 0
    BLACK = 1


def solve(m, n, rows: list[list[C]]) -> list[list[int]]:
    assert len(rows) == m
    assert len(rows[0]) == n

    flip = None

    def get(i, j) -> C:
        assert i < n
        assert j < m
        c = rows[j][i]
        for x, y in ((i + dx, i + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
            if not (0 <= x and 0 <= y and x < n and y < m):
                continue
            if flip[y][x]:
                c = 1 - c
        return c

    def calc_second_row_and_below(first_row) -> bool:
        nonlocal flip
        for j in range(1, m):
            for i in range(n):
                if (j == 1 and first_row[i] == C.BLACK) or (get(i, j - 1) == C.BLACK):
                    flip[j][i] = 1

        # check if the last line has no BLACK
        for i in range(n):
            if get(i, m - 1) == C.BLACK:
                return False
        return True

    def gen_first_row() -> Iterable[tuple[int]]:
        return itertools.product([0, 1], repeat=n)

    for first in gen_first_row():
        flip: list[list[int]] = [[0] * n for _ in range(m - 1)]
        flip.insert(0, list(first))
        # m行n列
        assert len(flip) == m
        assert len(flip[0]) == n

        if calc_second_row_and_below(first):
            return flip
    return "IMPOSSIBLE"


class Test(unittest.TestCase):
    def test_solve(self):
        m0 = a0 = [[0, 0, 0, 0]] * 3
        m1 = [[1, 1, 1, 1]] * 3
        m2 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
        a2 = [[0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]]
        tests = [
            ((4, 4, m2), a2),
            ((3, 4, m0), m0),
            # ((3, 4, m1), m0),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want

    def test_dictionary_order(self):
        got = list(itertools.product([0, 1], repeat=2))
        want = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
