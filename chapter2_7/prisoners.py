import unittest
import math


def solve_rec(p: int, q: int, a: list[int]) -> int:
    """金貨の枚数"""

    # メモ化再帰
    memo = {}

    def rec(start, stop) -> int:
        """開区間(start, stop) の囚人（間に空白なし）を解放するのに必要なコインの数を返す"""
        assert start < stop
        if (start, stop) in memo:
            return memo[start, stop]

        min = math.inf
        for k in [k for k in a if start < k and k < stop]:  # 区間のフィルタにO(q)かかる
            cost_first_k = rec(start, k) + rec(k + 1, stop) + (stop - start - 2)
            if cost_first_k < min:
                min = cost_first_k

        # 区間に囚人がいなかったら0
        if math.isinf(min):
            return 0

        memo[start, stop] = min
        return min

    return rec(0, p + 1)


def solve_dp(p: int, q: int, a: list[int]) -> int:  # aは1-indexで値が入っている
    assert len(a) == q
    # 端を追加
    a = [0] + a + [p + 1]

    # dp[i,j] := 開区間(i,j) の囚人を開放するコスト 間に空白無し
    #   答えはdp[0, p+1]
    dp = [[0 for i in range(q + 2)] for j in range(q + 2)]

    # 更新の順は対角成分に近い順
    #   (0,2) (1,3) .. (2,4), (0,3) (1,4) ..
    for w in range(2, q + 1):
        for i in range(q + 1):
            j = i + w

            # dp[i][j]の計算
            t = 9999999
            for k in range(i + 1, j):
                t = min(t, dp[i][k] + dp[k][j])

            dp[i][j] = t + a[j] - a[i] - 2

    return dp[0][q + 1]


class Test(unittest.TestCase):
    tests = [
        ((8, 1, [3]), 7),
        ((20, 3, [3, 6, 14]), 35),
    ]

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve_rec(*args) == want

    @unittest.skip("todo")
    def test_solve_dp(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve_dp(*args) == want


if __name__ == "__main__":
    unittest.main()
