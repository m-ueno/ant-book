import unittest


def solve(_n, k, L: list[float]) -> float:
    # 最大値を求める
    # conditionを満たせば ok xを上げる
    # -----ok|ng------

    def valid(x: float) -> bool:
        acc = 0
        for l in L:
            acc += l // x
            if acc >= k:
                return True
        return False

    ok = 0.
    ng = max(L) + 0.01

    while ng - ok > 1e-4:
        mid = (ok + ng) / 2
        if valid(mid):
            ok = mid
        else:
            ng = mid

    return round(ok, 2)


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ((4, 11, [8.02, 7.43, 4.57, 5.39]), 2.00),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
