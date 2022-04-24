import unittest


def solve(a, S) -> int:
    s = t = sum = 0
    n = len(a)
    lowest = int(1e9)

    while True:
        while sum < S and t < n:
            sum += a[t]
            t += 1
        if sum < S:
            return lowest
        while sum >= S:
            lowest = min(lowest, t - s)
            sum -= a[s]
            s += 1


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15), 2),
            (([1, 2, 3, 4, 5], 5), 1),
            (([1], 1), 1),
            (([1, 2, 1], 3), 2),
            (([1, 2, 1], 4), 3),
            (([1, 2, 3, 3, 3, 2, 2, 1, 1], 14), 6),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
