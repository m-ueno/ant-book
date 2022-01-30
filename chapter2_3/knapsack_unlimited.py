from __future__ import annotations
from typing import DefaultDict
import unittest
from pprint import pprint


def solve(ws: list[int], vs: list[int], capacity: int) -> int:
    """個数なしナップザック 何個選んでもいい

    n,w,v~100
    capacity~10000

    dp[i+1][j] := i番目(i=0,1,..) までで重さj以下で価値の総和の最大値
        ans = dp[n][j]
    dp[0][j]=0
    dp[i+1][j]
        = dp[i][j] | dp[i][j-w] + v | dp[i][j-2w]+2v | ...
        # dp[i][j]に加えてi+1番目の荷物をk個詰める

    計算量
    ----
    3重ループ
    O(n*W*W) 1e(3+4*2)=1e11 は間に合わない
    """
    n = len(ws)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(n):
        for j in range(capacity + 1):
            k = 0
            while k * ws[i] <= j:
                dp[i + 1][j] = max(
                    dp[i + 1][j],
                    dp[i][j - k * ws[i]] + k * vs[i],
                )
                # dp[i + 1][j] = max(
                #     dp[i][j],
                #     dp[i][j - ws[i]] + vs[i],
                #     # (i+1)からループするかもしれない->
                # 　　    これは間違い dp[i]までに加えてi+1番目の荷物をk個詰めると考える
                #     dp[i + 1][j - ws[i + 1]] + vs[i + 1],
                # )
                k += 1

    return dp[n][capacity]


def solve2(ws: list[int], vs: list[int], capacity: int) -> int:
    """
    dp[i+1][j] := i番目(i=0,1,..) までで重さj以下で価値の総和の最大値
        ans = dp[n][j]
    dp[0][j]=0
    dp[i+1][j]
        = dp[i][j] | dp[i][j-w] + v | dp[i][j-2w]+2v | ...
        # dp[i][j]に加えてi+1番目の荷物をk個詰める
        = max(dp[i][j-kw]+kv | 0<=k)
        1<=kの部分はループしなくても最大のがわかる
        = max(dp[i][j], dp[i+1][j-w] + v)
                          ^^^^^
    """

    n = len(ws)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(n):
        for j in range(capacity + 1):
            if j - ws[i] < 0:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(
                    dp[i][j],
                    dp[i + 1][j - ws[i]] + vs[i],
                )
    return dp[n][capacity]


class Test(unittest.TestCase):
    tests = [
        ((solve, [3, 4, 2], [4, 5, 3], 7), 10),
        ((solve2, [3, 4, 2], [4, 5, 3], 7), 10),
        #
    ]

    def test_solve(self):
        for i, ((f, w, v, cap), want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert f(w, v, cap) == want


if __name__ == "__main__":
    unittest.main()
