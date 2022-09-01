import unittest
from math import inf


def fib(n) -> int:
    # n=0,1,2,3 fib=0,1,1,2,...
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


M = list[list[int]]


def mul(a: M, b: M) -> M:
    # (n,k) * (k, m) -> (n, m)
    n = len(a)
    k = len(a[0])
    m = len(b[0])
    c = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for x in range(k):
                c[i][j] += a[i][x] * b[x][j]
    return c


def pow(a: M, n: int) -> M:
    # (m, m)
    m = len(a)
    acc = [[0] * m for _ in range(m)]
    for i in range(m):
        acc[i][i] = 1

    while n:
        if n & 1:
            acc = mul(acc, a)
        a = mul(a, a)
        n >>= 1
    return acc


def solve(n) -> int:
    a: M = [[1, 1], [1, 0]]
    a = pow(a, n)
    return a[0][1]


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (0, 0),
            (1, 1),
            (2, 1),
            # (3, 2),
            # (5, 22),
            (10, 55),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(args) == want

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


if __name__ == "__main__":
    unittest.main()
