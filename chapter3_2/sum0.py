import unittest
from itertools import product
from bisect import bisect_left, bisect_right


def solve(n, a: list[int], b: list[int], c: list[int], d: list[int]) -> int:
    # n~4000
    ab = sorted([x + y for x, y in product(a, b)])
    cd = sorted([x + y for x, y in product(c, d)])
    return sum(bisect_right(cd, -sum1) - bisect_left(cd, -sum1) for sum1 in ab)


class Test(unittest.TestCase):
    def test_solve(self):
        a = [-45, -41, -36, -36, 26, -32]
        b = [22, -27, 53, 30, -38, -54]
        c = [42, 56, -37, -75, -10, -6]
        d = [-16, 30, 77, -46, 62, 45]
        tests = [((6, a, b, c, d), 5)]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
