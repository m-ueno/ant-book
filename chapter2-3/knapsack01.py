from typing import Any, DefaultDict
import unittest
from pprint import pprint
from collections import defaultdict


def solve(ws: list[int], vs: list[int], capacity: int) -> int:
    """0-1 Knapsack"""
    n = len(ws)
    memo = {}

    def rec(i, cap) -> int:
        if (i, cap) in memo:
            return memo[(i, cap)]
        if i == n:
            return 0
        w, v = ws[i], vs[i]

        print(i, cap)
        if w > cap:
            # はいらない
            acc = rec(i + 1, cap)
        else:
            acc = max(rec(i + 1, cap - w) + v, rec(i + 1, cap))
        memo[(i, cap)] = acc
        return acc

    return rec(0, capacity)


def dp(ws: list[int], vs: list[int], capacity: int) -> int:
    """動的計画法

    dp[i][cap]
    ★解は dp[0][cap]
        solveでは rec(0, capacity) で再帰計算した
    かわりにボトムアップに計算する

    1.dp[n][cap] = 0  # もうない
    2.dp[i][cap] =
      dp[i+1][cap]   (if w[i]>cap)
        or
      max(
          dp[i+1][cap-w[i]] + v[i],
          dp[i+1][cap]
      )
    の漸化式を i=nからn-1,n-2,...と逆順にとく
    """
    n = len(ws)
    dp = [[-1] * (capacity + 1) for i in range(n + 1)]
    for j in range(capacity + 1):
        dp[n][j] = 0

    i = n - 1
    j = 0
    while i >= 0:
        for j in range(capacity + 1):
            w, v = ws[i], vs[i]
            if w > j:
                # いっぱいで入らない
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = max(
                    dp[i + 1][j],
                    dp[i + 1][j - w] + v,
                )
        i -= 1

    pprint((i, j, dp))
    return dp[0][capacity]


def dp2(ws: list[int], vs: list[int], capacity: int) -> int:
    """順方向に埋める版

    dp[i+1][j] := i番目「まで」の品物から重さの総和がj以下となるようにとったときの価値の最大値
        (ans == dp[n][W])
        i+1で「iまで」の定義がトリッキー
    dp[0][j] = 0
    dp[i+1][j]
        = dp[i][j]  (w[i]>j もう入らないとき)
        or
        = max(dp[i][j], dp[i][j-wi]+vi
    """
    n = len(ws)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # i+1==n <=> i = n-1
    for i in range(n):
        for j in range(capacity + 1):
            wi, vi = ws[i], vs[i]
            if wi > j:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - wi] + vi)
    pprint(dp)
    return dp[n][capacity]


def dp3(ws: list[int], vs: list[int], capacity: int) -> int:
    """漸化式の後ろを場合分けするのでなく、前を場合分けする版

    dp[i+1][j] := i番目まで使って総和がjまでで最大の価値
    (i,j)
        -> (i+1,j)
        and/or
        -> (i+1,j+w)
    ans = dp[n][W]
    """
    n = len(ws)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(capacity + 1):
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
            if j + ws[i] <= capacity:
                dp[i + 1][j + ws[i]] = dp[i][j] + vs[i]  # テキストだとmaxつけてあるけど多分不要
    return dp[n][capacity]


def dp_array(ws: list[int], vs: list[int], capacity: int) -> int:
    """
    漸化式dp[i+1]のアップデートにdp[i]しか使わないので
    （dp[i-2], dp[i-3], ...はいらない）
    1つの配列を使いまわせばよい

    dp[i+1][j] := e_0..e_iを使って総和がjまでで価値の最大値
    """
    n = len(ws)
    dp = [0] * (capacity + 1)
    for i in range(n):
        j = capacity
        while j >= ws[i]:
            dp[j] = max(dp[j], dp[j - ws[i]] + vs[i])
            j -= 1

    return dp[capacity]


def dp_heavy_cargo(ws: list[int], vs: list[int], capacity: int) -> int:
    """荷物が重い場合.

    n~100
    w[i] ~ 1e7
    よこにwを並べられないので
    セルの中をそこまでのweightにする
    dp[i+1][j] := 荷物e0...e_iを使って価値の総和がjとなる、重量の最小値
        ans: dp[n][j] <= capacityを満たす最大のj
    dp[0][0] = 0
    dp[0][j] = inf ★
    dp[i][0] = 0
    dp[1][j]
        = dp[1][v[i]]
        = w[i]
    dp[i+1][j]
        = dp[i][j] （e_{i+1}を選ばない. 価値も重量も変わらない）
        or
        = dp[i][j - v[i]] + w[i]
            もしこれがcapacity超えだったら..
            このあと何を足してもcapacity超えなのでinfをいれておけばよい？
    """
    n = len(ws)
    from math import inf

    dp = defaultdict(lambda *args: inf)
    dp[0, 0] = 0  # ★

    for i in range(n):
        for j in range(sum(vs) + 1):
            if j - vs[i] < 0:
                dp[i + 1, j] = dp[i, j]
            else:
                dp[i + 1, j] = min(dp[i, j], dp[i, j - vs[i]] + ws[i])

    # capacityを超えない最大の総和j
    #   infが途中にあるかもしれないので二分探索は使えない
    j = sum(vs) + 1
    while True:
        if dp[n, j] <= capacity:
            break
        j -= 1
    return j


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (([2, 1, 3, 2], [3, 2, 4, 2], 5), 7),
        ]
        for f in [dp_heavy_cargo, solve, dp, dp2, dp3, dp_array]:
            with self.subTest(f"{f}"):
                for i, ((w, v, cap), want) in enumerate(tests):
                    with self.subTest(f"i={i}"):
                        got = f(w, v, cap)
                        assert got == want


if __name__ == "__main__":
    unittest.main()
