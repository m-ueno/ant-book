from __future__ import annotations
import unittest


def solve(n, m, a: list[int], M) -> int:
    """重複組み合わせ (3重ループ)

    n種類の品物
    a_i個まで
    合計m個
    n,m,a_i~1000

    計算量
    ----
    O(n*m*m) = 1e9

    dp[i+1, j] := i番目までの品物からj個選ぶ組み合わせの総数  # 右辺は1-origin
        ans = dp[n][m]
            i+1==nのときi=n-1
    dp[0, j] = 0
    dp[i, 0] = 1
    dp[i+1, j] = dp[i, j]  # i-1番目までをjこ、i番目を0こ
        + dp[i, j-1] i-1番目までをj-1こ、i番目を1こ選ぶ
        + dp[i, j-2] i-1番目までをj-2こ、i番目を2こ選ぶ
        + dp[i, j-j] i-1番目までをj-jこ、i番目をjこ選ぶ
        = dp[i+1, j] = Σ_{k=0}^{min(j, a[i])} dp[i, j-k]

        j <= a[i]のときk=0..j
        a[i] < jのとき k=0..a[i] (j個選べない)

        k = 0...min(j,a[i])
        と動くときjの範囲は
        j = j-k+1...j
        左端の座標は

    dp[1, j] = 1 if j<=1番目(a_0) or 0 (a_0<j)
    """
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(n):
        for j in range(1, m + 1):
            acc = 0
            # rangeはstopを含まないので+1する
            for k in range(min(a[i], j) + 1):
                acc += dp[i][j - k]
            dp[i + 1][j] = acc % M

    return dp[n][m] % M


def solve_reuse(n, m, a, M) -> int:
    """O(nm)の解法

               j
       .............
    i  ...ABBBCD(i, j)
    i+1.......YX(i+1,j)

    a[i] = 4, X = (i+1, j)のとき上図から
    D = (i, j)のとき
    B左端 = (i, j-a[i])
    A = (i, j-a[i]-1)
    k = [0, 4]

    dp[X]をもとめるのにdp[Y]を使いまわす

    場合分け
    - j-1がa[i]に比べて小さいときはdp[Y] =   B+B+B+C (Aが足されない)
        dp[X] = dp[Y] + dp[D]
    - j-1がa[i]に比べて大きいときはdp[Y] = A+B+B+B+C
        dp[X] = B+B+B+C+D = dp[Y] - dp[A] + dp[D]

    ref. https://scrapbox.io/pocala-kyopro/%E8%9F%BB%E6%9C%AC_p.67
    """
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):  # 間違えてrange(n)とすると最後の行が1ずつ小さくなる
        dp[i][0] = 1
    for i in range(n):
        for j in range(1, m + 1):
            if j - 1 < a[i]:
                # 左が詰まってるのでdp[A]は除かずdp[D]だけ足す
                dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % M
            else:
                lower = j - 1 - a[i]
                dp[i + 1][j] = (dp[i + 1][j - 1] - dp[i][lower] + dp[i][j]) % M

    return dp[n][m]


class Test(unittest.TestCase):
    tests = [((3, 3, [1, 2, 3], 10000), 6)]  # n,m,a,modulo

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(*args) == want

    def test_solve_reuse(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve_reuse(*args) == want


if __name__ == "__main__":
    unittest.main()
