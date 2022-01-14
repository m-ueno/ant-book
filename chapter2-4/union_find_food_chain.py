from __future__ import annotations
from typing import Union
import unittest

from union_find_tree import UnionFindTree


def solve(n: int, k: int, info: list[tuple[int, int, int]]) -> int:
    """食物連鎖 以前に与えられた情報と矛盾する個数を返す

    N~50000
    K~100000

    タイプ1の情報: xとyは同じ種類の動物です
        正しいなら (x,y) = (A,A) or (B,B) or (C,C)
    タイプ2の情報: xはyを食べます
        正しいなら (x,y) = (A,B) or (B,C) or (C,A)
    """
    assert k == len(info)

    tree = UnionFindTree(3 * n)
    acc = 0

    for i in range(k):
        typ, x, y = info[i]
        x = x - 1
        y = y - 1
        if not (0 <= x < k and 0 <= y < k):
            acc += 1
            continue

        if typ == 1:
            if tree.same(x, y + n) or tree.same(x, y + 2 * n):
                acc += 1
            else:
                tree.unite(x, y)
                tree.unite(2 * x, 2 * y)
                tree.unite(3 * x, 3 * y)
        elif typ == 2:
            if tree.same(x, y) or tree.same(x, y + 2 * n):
                acc += 1
            else:
                # i-Aがj-Bを食べる or i-Bがj-Cを食べる or i-Cがj-Aを食べる
                tree.unite(x, y + n)
                tree.unite(x + n, y + 2 * n)
                tree.unite(x + 2 * n, y)
        else:
            raise Exception("panic")

    return acc


class Test(unittest.TestCase):
    tests = [
        (
            (
                100,
                7,
                [
                    (1, 101, 1),
                    (2, 1, 2),
                    (2, 2, 3),
                    (2, 3, 3),
                    (1, 1, 3),
                    (2, 3, 1),
                    (1, 5, 5),
                ],
            ),
            3,
        ),
    ]

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
