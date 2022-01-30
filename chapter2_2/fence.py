from __future__ import annotations

import unittest
from collections import Counter
from typing import Any, Optional
from heapq import heappop, heappush


def solve(xs: list[int]) -> int:
    """
    解答
    ---
    小さいほうからまとめていく
    木の末端から上に上る
    """
    h = []
    for x in xs:
        heappush(h, x)

    acc = 0
    while len(h) > 1:
        a, b = heappop(h), heappop(h)
        acc += a + b
        heappush(h, a + b)
    assert len(h) == 1
    return acc


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ([8, 5, 8], 34),
            ([2], 0),
            ([2, 2], 4),
            ([2, 2, 2, 2], 16),
            ([1, 2, 3, 4, 5], 3 + 6 + 9 + 15),
        ]
        for i, (*args, want) in enumerate(tests):
            with self.subTest(i=i):
                got = solve(*args)
                self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
