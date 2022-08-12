import unittest
from math import inf


def solve_rec(n, d) -> int:
    """メモ化再帰"""

    memo = {}

    def rec(seen: frozenset[int], v: int) -> int:
        # v: seenにある着目している頂点

        # ok
        if (seen, v) in memo:
            return memo[seen, v]

        # 全部訪問済み
        if len(seen) == n and v == 0:
            memo[seen, v] = 0
            return 0

        min_cost = inf
        for u in range(n):
            if len(seen) == n and u == 0:
                memo[seen, v] = 0
                return 0
            if u not in seen:  # この条件が、最後にu=0のとき成り立たないので、返ってこない
                min_cost = min(min_cost, rec(seen | {u}, u) + d[v][u])
        memo[seen, v] = min_cost

        return min_cost

    return rec(frozenset(), 0)


class Test(unittest.TestCase):
    def test_solve(self):
        g = [
            (0, 1, 3),
            (0, 3, 4),
            (1, 2, 5),
            (2, 0, 4),
            (2, 3, 5),
            (3, 4, 7),
            (4, 1, 6),
            (4, 0, 7),
        ]
        d = [[inf] * 5 for _ in range(5)]
        for i, j, w in g:
            d[i][j] = w

        tests = [
            ((5, d), 22),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve_rec(*args) == want


if __name__ == "__main__":
    unittest.main()
