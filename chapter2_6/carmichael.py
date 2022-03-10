from __future__ import annotations
import unittest
from math import sqrt, ceil


def isprime(n) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


primes = [x for x in range(2, 65000) if isprime(x)]


def modpow(x: int, n: int, mod: int) -> int:
    ans = 1
    while n > 0:
        if n % 2 == 0:
            x *= x
            n //= 2
        else:
            ans *= x
            ans %= mod
            n -= 1
    return ans


def solve(n: int) -> bool:
    # フェルマーテストの結果を返す
    # 素数はFalse
    if isprime(n):
        return False
    for x in range(2, n):
        if modpow(x, n, n) != x:
            return False
    return True


def solve2(n: int) -> bool:
    """奇数の合成数がカーマイケル数であるための必要十分条件 を使う
    https://math.cs.kitami-it.ac.jp/~kouno/kougi/crypto11_09.pdf
    """
    m = n
    # (0)
    if isprime(n):
        return False
    # (1)素因数分解
    factors = []
    for p in primes:
        if m == 1:
            break
        if m % p == 0:
            m //= p
            if m % p == 0:
                return False
            factors.append(p)

    assert len(factors) > 1, len(factors)

    # (2)
    for p in factors:
        if (n - 1) % (p - 1) != 0:
            return False
    return True


class Test(unittest.TestCase):
    tests = [
        (3, False),  # 3は素数
        (4, False),
        (17, False),
        (561, True),
        (2821, True),
    ]

    def test_modpow(self):
        tests = [
            ((2, 2), 4),
            ((3, 2), 9),
            ((9, 17), 9**17 % 17),
        ]
        for ((x, n), want) in tests:
            assert modpow(x, n, 17) == want

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(args) == want

    def test_solve2(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve2(args) == want
        for i in range(4, 561):
            assert solve2(i) == False


if __name__ == "__main__":
    unittest.main()
