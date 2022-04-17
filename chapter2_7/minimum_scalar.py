import unittest


def solve(v: list[int], w: list[int]) -> int:
    """内積の最小値を返す"""
    v = sorted(v)
    w = sorted(w, reverse=True)
    return sum(x * y for x, y in zip(v, w))


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (([1, 2], [3, 4]), 10),
            (([1, 3, -5], [-2, 4, 1]), -25),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
