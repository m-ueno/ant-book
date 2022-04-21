import unittest


def solve(n, m, xs: list[int]) -> int:
    # 最大値を求める
    # -----ok|ng------

    xs = sorted(xs)

    def valid(d: int) -> bool:
        next = xs[0] + d
        put = 1

        for i in range(1, n):
            if next <= xs[i]:
                next = xs[i] + d
                put += 1
                if put == m:
                    return True
        return False

    ok = 0
    ng = max(xs)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if valid(mid):
            ok = mid
        else:
            ng = mid

    return ok


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ((5, 3, [1, 2, 8, 4, 9]), 3),
            ((5, 2, [1, 2, 8, 4, 9]), 8),
            ((9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9]), 4),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
