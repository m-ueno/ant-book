from abc import ABC, abstractmethod
import unittest


class BIT:
    def __init__(self, xs: list[int]):
        self.bit = [0] * (len(xs) + 1)
        self.n = len(xs)
        for i, x in enumerate(xs):
            self.add(i + 1, x)

    def add(self, i: int, x: int):
        """区間iから初めて、右端bitだけ立っている数を加算しながら、区間iにxを足す

        x & -x は立っている一番右端のビットだけ残して0にしてしまう黒魔術
        https://siokoshou.hatenadiary.org/entry/20090704/p1
        """
        assert 1 <= i <= self.n
        while 1 <= i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i: int) -> int:
        """a1+a2+...+a_iを返す"""
        acc = 0
        while i > 0:
            acc += self.bit[i]
            i -= i & -i
        return acc


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tree1 = BIT([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_create(self):
        assert self.tree1.n == 9

    def test_query(self):
        tests = [
            (1, 1),
            (2, 3),
            (3, 6),
            (4, 10),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert self.tree1.sum(args) == want
