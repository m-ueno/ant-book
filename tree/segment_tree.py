from math import floor, inf, log2
import unittest


class RangeMinimumQuery:
    def __init__(self, xs: list[int]):
        depth = floor(log2(len(xs)))
        # 配列要素数は全体で2n - 1
        n = 1
        while len(xs) > n:
            n *= 2

        self.n = n  # 葉の数 (2^xに水増ししたもの)
        self.data = [0] * (2 * n - 1)
        for i, x in enumerate(xs):
            self.update(i, x)

    def update(self, i: int, x: int):
        i += self.n - 1
        self.data[i] = x

        # rootまで親を更新
        while i > 0:
            i = (i - 1) // 2
            self.data[i] = min(self.data[i * 2 + 1], self.data[i * 2 + 2])

    def query(self, s: int, t: int) -> int:
        """半開区間 [s, t) の最小値"""
        return self._query(s, t, 0, 0, self.n)

    def _query(self, s, t, k: int, l: int, r: int) -> int:
        # k: 見ているノードの位置
        # [l, r): self.data[k]が表している区間
        if r <= s or t <= l:  # (1) 範囲外
            return inf
        elif s <= l and r <= t:  # (2) 完全にこのノードの範囲に収まる
            return self.data[k]
        else:
            vl = self._query(s, t, k * 2 + 1, l, (l + r) // 2)
            vr = self._query(s, t, k * 2 + 2, (l + r) // 2, r)
            return min(vl, vr)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tree1 = RangeMinimumQuery([3, 5, 2, 4])

    def test_create(self):
        assert len(self.tree1.data) == 2 * 4 - 1

    def test_query(self):
        tests = [
            ((0, 4), 2),
            ((0, 2), 3),
            ((1, 2), 5),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert self.tree1.query(*args) == want
