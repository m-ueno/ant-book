from __future__ import annotations
import unittest


def solve(n, m, M) -> int:
    """分割数
    n個の同種のもの
    mグループ以下に分割
    場合の数をMでわった余り

    dp(m, n) := nをm群以下に分割する場合の数
        = dp(m-1, n) + ちょうどm群に分割する場合の数
        = dp[m-1, n] + dp[m, n-m]
                       ^^^^^^^^^^★

        ★nをちょうどm群に分割する場合の数は、n-mをm群以下に分割する場合の数に等しい
            ^^^^^^^^^^                         ^^^^^
            具体例で考えるとわかる。各群から1ずつひいて考える

    dp[1, n] = 1
    dp[m, 1] = 1

    dpテーブルを見るとm=nのときの値がおかしい.
    例で考えてみると,
    dp[2,2] = 2の2分割以下
        = 2の1分割 + 2のちょうど2分割
        = 1 + 1
        = dp[1, 2] + dp[2, 0]
        dp[2,0]は1にならないとだめ

    dp[i, 0] := 1


    Wikipediaの別解
    ------
    k以上の自然数を用いてnを分割する場合の数 p(k,n) を考える
    分割を場合分け
        1. 最小の成分がk
        2. 最小の成分がkより大きい

        1.の場合の数は、最小の成分を1つ除いた場合の数 p(k,n-k)と等しい。末尾にkを足したらいいので
        2.の場合の数は、p(k+1, n)に等しい
            k以上を用いた場合の数から、ちょうどkの場合の数を除いたものは、k+1以上を用いた場合の数になる

        k,n=5,15とすると、15 =5+5+5 =5+10 =6+9 =7+8
        p(5,15) = p(5, 10) + p(6, 15) = 2+2 = 4

        p(k,n) = p(k,n-k) + p(k+1,n)
        ans = p(1,n)
    """
    dp = [[0] * (n + 1) for i in range(m + 1)]
    dp[0][0] = 1
    for i in range(1, m + 1):
        for j in range(0, n + 1):
            if j - i < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % M

            #
            # 上のようにdp[0][0]=1とすれば下の場合分けが減らせる
            #
            # if i == 1:
            #     dp[i][j] = 1
            # elif j - i < 0:
            #     dp[i][j] = dp[i - 1][j]
            # elif j == i:
            #     dp[i][j] = (dp[i - 1][j] + 1) % M
            # else:
            #     dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % M

    return dp[m][n]


class Test(unittest.TestCase):
    tests = [((4, 3, 10000), 4)]  # n,m,modulo

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(f"i={i}"):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
