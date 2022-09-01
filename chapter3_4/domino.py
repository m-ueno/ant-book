import unittest
from math import inf

W = 0
B = 1


def solve(n: int, m: int, board: list[list[int]]) -> int:
    # for _ in range(n):
    #     for _ in range(m):
    #         dp.append([0] * (2**m))

    # dp: パターンの総数
    dp: list[list[list[int]]] = [[[0] * (2**m) for _ in range(m)] for _ in range(n)]
    assert len(dp) == n
    assert len(dp[0]) == m
    assert len(dp[0][0]) == 1 << m

    dp[0][0][0] = 1  # 1通り
    for i in range(n):
        for j in range(m):
            for s in range(1 << m):
                # (i, j)に置けないとき
                if (s & (1 << j)) or board[i][j] == B:
                    s_next = s & ~(1 << j)
                    dp[i][(j + 1) % m][s_next] += dp[i][j][s]
                else:
                    # 横置き
                    if j + 1 < m and board[i][j + 1] == W and not (s & (1 << (j + 1))):
                        s_next = s | (1 << (j + 1))
                        dp[i][j + 1][s_next] += dp[i][j][s]
                    if i + 1 < n and board[i + 1][j] == W:
                        s_next = s | (1 << j)
                        dp[i][(j + 1) % m][s_next] += dp[i][j][s]

    return dp[n - 1][m - 1][1 << m - 1]


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ((3, 3, [[W, W, W], [W, B, W], [W, W, W]]), 2),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
