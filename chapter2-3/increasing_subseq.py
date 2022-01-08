from __future__ import annotations
import unittest
from math import inf
from itertools import product


def solve(a: list[int]) -> int:
    """最長増加部分列問題 O(n^2)

    n~1000
    a_i~1e7
    2重ループはOK

    dp[i] := 最後がa_iで終わる最長の増加部分列の長さ
    dp[i]
        = a_iからのみなる列
        or
        = a_jで終わる部分列の末尾にa_iを付け足した列 (if a_j<a_i)
    """
    n = len(a)
    dp = [-1] * n
    dp[0] = 1
    for i in range(n):
        tmp = 1
        for j in range(i):
            if a[j] < a[i]:
                tmp = max(tmp, dp[j] + 1)
        dp[i] = tmp

    return dp[n - 1]


def lower_bound(xs, cond) -> int:
    """return lowest index that cond(x) == True"""
    return _lower(xs, cond, lo=0, hi=len(xs))


def _lower(xs, cond, lo, hi) -> int:
    while lo < hi:
        idx = (lo + hi) // 2
        if cond(xs[idx]):
            hi = idx
        else:
            lo = idx + 1
            # lo=idxとしてしまうと誤り. 長さ2になったときに無限ループ
    return lo
    # [0,1,2] lo,hi=0,3 m=1


def solve2(a: list[int]) -> int:
    """
    O(n log(n)) の解法

    dp[i] := 長さがi+1である増加部分列における最終要素の最小値

    dp[i]は単調増加になるので二分探索できる
        手でこのテーブルをつくれば気付けるかも
    """
    n = len(a)
    dp = [inf] * n

    for i in range(0, n):
        if i == 0 or dp[i - 1] < a[i]:
            dp[i] = min(dp[i], a[i])
        else:
            # dpのうちa[i]を超える最初＝最小のものを差し替え
            idx = lower_bound(dp, lambda mid: a[i] < mid)
            dp[idx] = a[i]

    # infの左端indexがLISの長さと等しい
    # dp=[1,3,5,inf,inf] -> 3
    return lower_bound(dp, lambda mid: mid is inf)


class Test(unittest.TestCase):
    def test_solve(self):
        fns = [solve, solve2]
        tests = [
            ([4, 2, 3, 1, 5], 3),
            ([2, 3, 1, 2, 3], 3),
            ([1, 100, 2, 201, 3], 3),
            ([10, 1, 11, 2, 12], 3),
        ]

        for i, (f, (a, want)) in enumerate(product(fns, tests)):
            with self.subTest(f"i={i}"):
                assert f(a) == want

    def test_lower(self):
        self.assertEqual(2, 2)
        assert lower_bound([0, 0, inf], lambda x: x == inf) == 2
        assert lower_bound([0, 0, inf, inf], lambda x: x == inf) == 2
        assert lower_bound([0, 0, inf, inf, inf], lambda x: x == inf) == 2


if __name__ == "__main__":
    unittest.main()
