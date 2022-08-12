import unittest
from .matrix import mul, pow


class Test(unittest.TestCase):
    def test_mul(self):
        e = [[1, 0], [0, 1]]
        x = [[1, 2], [3, 4]]
        self.assertEqual(e, mul(e, e))
        self.assertEqual(e, mul(mul(e, e), e))
        self.assertEqual(x, mul(e, x))
        self.assertEqual(x, mul(x, e))

        self.assertEqual(mul([[0, 1], [2, 3]], [[4], [3]]), [[3], [17]])

    def test_pow(self):
        e = [[1, 0], [0, 1]]
        tests = [
            ((e, 0), e),
            ((e, 2000), e),
            (([[2]], 0), [[1]]),
            (([[2]], 1), [[2]]),
            (([[2]], 2), [[4]]),
            (([[2]], 3), [[8]]),
            (([[2]], 10), [[1024]]),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert pow(*args) == want
