from __future__ import annotations
from math import sqrt, ceil, floor
import unittest


def primes(stop: int) -> list[int]:
    # 区間[2, stop)
    xs = [True] * stop
    xs[0] = xs[1] = False

    for i in range(2, ceil(sqrt(stop)) + 1):
        if xs[i]:
            j = 2
            while i * j < stop:
                xs[i * j] = False
                j += 1
    return [i for i, x in enumerate(xs) if x]


def n_primes(n: int) -> int:
    return len(primes(n + 1))


def interval(a, b: int) -> int:
    """a,b~1e12"""
    is_prime = [True] * (b - a)
    for p in primes(floor(sqrt(b))):
        i = max(2, ceil(a / p))  # [a,b)にはいるa<=p*iをみたすiの最小値

        while p * i < b:
            idx = p * i - a
            is_prime[idx] = False
            i += 1

    return sum(is_prime)


class Test(unittest.TestCase):
    def test_primes(self):
        tests = [
            (11, 5),
            (1000000, 78498),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert n_primes(args) == want

    def test_interval(self):
        tests = [
            ((22, 37), 3),
            ((22801763489, 22801787297), 1000),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert interval(*args) == want


if __name__ == "__main__":
    unittest.main()
