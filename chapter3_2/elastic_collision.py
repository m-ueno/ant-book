import unittest
from math import sqrt


def solve(N, H, R: float, T) -> list[float]:
    list_h0: list[float] = [H + 2 * R * i for i in range(N)]
    G = 10.0
    list_period = [sqrt(2 * h0 / G) for h0 in list_h0]

    def x(h0, period) -> float:
        t = T % period
        if (T // period) % 2 == 0:
            # 上昇中
            return G * t * t / 2.0
        else:
            # 下降中
            return h0 - G * t * t / 2.0

    list_x = [x(h0, p) for h0, p in zip(list_h0, list_period)]
    return list_x


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            # (N, H, R, T)
            ((1, 10, 0.1, 100), [4.95]),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
