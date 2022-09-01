import unittest

from matrix import pow, M

M = list[list[int]]


def solve(n) -> int:
    a: M = [[2, 1, 0], [2, 2, 2], [0, 1, 2]]
    a = pow(a, n)
    return a[0][0]


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ((1,), 2),
            ((2,), 6),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
