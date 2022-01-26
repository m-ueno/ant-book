import unittest


def solve(s: str, t: str) -> int:
    """lcs

    長さnの列sと長さmの列tが与えられる
        s1s2...sn 添え字は s0...s_n-1
        n,m ~1e3
    dp[i][j] := s_0..s_iまで(添え字i含まない)とt0..t_jまで(含まない)のLCSの長さ
        x dp[i][j] .. s_iまで(含む)とs_jまで(含む)のLCS とすると初期化が面倒
        x   dp[0][j]= 0 or 1
    dp[0][j] = 0
    dp[i][0] = 0
    dp[i+1][j+1]
        - s_i+1 == t_i+1なら dp[i][j]+1
        or
        - dp[i][j+1]
        or
        - dp[i+1][j]
    ans = dp[n][n]
    """
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for i in range(n + 1)]

    # i+1=n <=> i <= n-1
    for i in range(n):
        for j in range(m):
            # if (i + 1 < n) and (j + 1 < m) and s[i + 1] == t[j + 1]:
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[n][m]


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ("a", "a", 1),
            ("abcd", "becd", 3),
            ("ABABC", "BABCA", 4),
            ("ABABC", "ABCBA", 3),
        ]
        for i, (s, t, want) in enumerate(tests):
            with self.subTest(i=i):
                got = solve(s, t)
                assert got == want


if __name__ == "__main__":
    unittest.main()
