import unittest
from math import inf

from matrix import pow, M
from tree.segment_tree import RangeMinimumQuery


def solve_naive(n, m, st: list[tuple[int, int]]) -> int | float:
    dp: list[int | float] = [inf] * (n + 1)
    dp[1] = 0

    for s, t in st:
        dp[t] = min(dp[t], min(dp[s : t + 1]) + 1)

    return dp[n]


def solve(n, m, st: list[tuple[int, int]]) -> int | float:
    BIG_INT = int(1e9)
    dp = [BIG_INT] * (n + 1)
    dp[1] = 0

    rmq = RangeMinimumQuery(dp)

    for s, t in st:
        v = min(dp[t], rmq.query(s, t + 1) + 1)
        dp[t] = v
        rmq.update(t, v)

    return dp[n]


class Test(unittest.TestCase):
    def test_wrap(self, fn=solve):
        tests = [
            # n,m,(s,t)
            ((40, 6, [(20, 30), (1, 10), (10, 20), (20, 30), (15, 25), (30, 40)]), 4),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert fn(*args) == want

    def test_solve_naive(self):
        self.test_wrap(solve_naive)

    def test_solve(self):
        self.test_wrap(solve)


if __name__ == "__main__":
    unittest.main()
