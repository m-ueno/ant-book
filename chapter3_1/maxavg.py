import unittest


def solve(ws, vs, k) -> float:
    # 最大値を求める
    # -----ok|ng------

    def valid(x):
        xs = sorted([v - x * w for v, w in zip(vs, ws)], reverse=True)
        return sum(xs[:k]) >= 0

    ok = 0
    ng = 1e6
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
            (([2, 5, 2], [2, 3, 1], 2), 0.75),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
