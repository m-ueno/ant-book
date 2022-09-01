from __future__ import annotations
from textwrap import TextWrapper
import unittest
from math import sqrt, ceil


def isprime(n) -> True:
    if n % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def tetration(a, n):
    if n == 0:
        return 1
    else:
        return a ** tetration(a, n - 1)


def pow(x, n):
    ret = 1
    for i in range(n):
        ret *= x
        ret %= n
    return ret


def pow2(x, n):
    """x:=x^2 をn回繰り返す (mod n)"""
    for i in range(n):
        x = (x * x) % n
    return x


def pown(x, n) -> bool:
    """
    pow(x, n) % n を高速計算する

    n = f(2, p) * q + r とあらわす最大のpを見つけると
    x^n = (x^f(2,p))^q * x^r となってべき乗計算が最小回数で済む
    """
    p = 0
    for p in range(10):
        if tetration(2, p + 1) > n:
            break
    q, r = divmod(n, tetration(2, p))
    return pow(pow2(x, p), q) * pow(x, r) % n


def solve(n: int) -> bool:
    """
    任意の1<x<n < 65000
    x^n = x (mod n)
    が成り立つような非素数nかどうか
    まず素数ならFalse.
    """
    for x in range(2, n):
        if pown(x, n) != x:
            return False
    return True


class Test(unittest.TestCase):
    def test_pow(self):
        tests = [
            ((2, 3), 8 % 3),
            ((3, 5), 3**5 % 5),
        ]
        for ((x, n), want) in tests:
            assert pow(x, n) == want

    def test_pow2(self):
        # x := x^2
        tests = [
            ((2, 2), 2**2**2 % 2),
            ((3, 2), 3**2**2 % 2),
            #
            ((2, 3), 2**2**2**2 % 3),
            ((7, 3), 7**2**2**2 % 3),
            ((11, 3), 11**2**2**2 % 3),
        ]
        for ((x, n), want) in tests:
            assert pow2(x, n) == want

    def test_solve(self):
        tests = [
            (3, False),  # 3は素数
            (4, False),
            (17, False),
            (561, False),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(args) == want


if __name__ == "__main__":
    unittest.main()
