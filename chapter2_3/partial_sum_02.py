from __future__ import annotations
import unittest


def solve(a: list[int], m: list[int], target) -> int:
    """個数制限付き部分和問題

    ナップサックと違いぴったりじゃないとだめ
    個数制限あり 0<=k<=mi
    全探索するとn*2^m
        n~100
        a_i,m_i~1e6
        K~1e6

    dp[i+1][j] := [0,i+1)まででjを作れるか
        boolをもってもよいが無駄
    3重ループ
        n*K*a_i ~ 1e14

    dp[i+1][j] := jを作る際に余る最大のi番目の個数（作れない場合は-1）
    dp[i+1][j]
        = m[i] (iまででjができてたら全部残せる)
        = -1 (1個でも足すと超えてしまう|1個足しても作れない)
        = dp[i+1][j-a[i]] - 1
            使うやつはおなじ. 和をずらす
    計算量
    ------
    O(nK) ~ 1e8
    """
    n = len(a)
    dp = [[-1] * (target + 1) for i in range(n + 1)]
    dp[0][0] = 0  # ★
    # jが0
    # for i in range(n):
    #     dp[i + 1][0] = m[i]
    for i in range(0, n):
        for j in range(target + 1):
            if dp[i][j] >= 0:  # ★等号も許す
                dp[i + 1][j] = m[i]
            else:
                if a[i] > j or dp[i + 1][j - a[i]] <= 0:
                    dp[i + 1][j] = -1
                else:
                    dp[i + 1][j] = dp[i + 1][j - a[i]] - 1

                # if j - a[i] >= 0 and dp[i + 1][j - a[i]] >= 0:
                #     dp[i + 1][j] = dp[i + 1][j - a[i]] - 1 　# 非負になるよう場合分け必要

    return dp[n][target]


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (([3, 5, 8], [3, 2, 2], 17), True),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                got = solve(*args)
                assert got > 0, got


if __name__ == "__main__":
    unittest.main()
