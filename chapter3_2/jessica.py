import unittest


def solve(a: list[int], P: int) -> int:
    s = t = 0
    m = {}  # map(要素a_i => 右端に出現するa_iのindex)
    nilCount = len(set(a))
    lowest = int(1e9)

    while True:
        while nilCount > 0 and t < P:
            if a[t] not in m:
                nilCount -= 1
            m[a[t]] = t
            t += 1
        if nilCount > 0:
            return lowest
        while nilCount == 0 and s < P:
            lowest = min(lowest, t - s)
            if m[a[s]] == s:
                nilCount += 1
                m[a[s]] = None
            s += 1


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (([1, 8, 8, 8, 1], 5), 2),
            #
            (([1, 3, 2], 3), 3),
            (([1, 1, 1, 1], 4), 1),
            (([1, 1, 2, 2], 4), 2),
            (([3, 3, 2, 3], 4), 2),
            (([1, 1, 2, 3], 4), 3),
            (([3, 1, 2, 3], 4), 3),
            (([1, 3, 3, 2], 4), 4),
            (([1, 1, 3, 3, 2, 4], 6), 5),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
