from __future__ import annotations
import unittest


def gcd(a: int, b: int) -> int:
    # if a < b:
    #     a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


def gcdext(a: int, b: int) -> tuple[int, int, int]:
    # if a < b:
    #     a, b = b, a
    r = a % b
    if r == 0:
        # aをbで割ったあまりが0
        # 例： a,b=12,3
        # 12x+3y=3を満たすx,yは x,y=0,1
        return 0, 1, b
    x1, y1, d = gcdext(b, r)
    return y1, x1 - a // b * y1, d


class Test(unittest.TestCase):
    def test_gcd(self):
        tests = [
            ((1, 4), 1),
            ((4, 12), 4),
            ((24, 15), 3),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert gcd(*args) == want

    def test_gcdext(self):
        tests: list[tuple[tuple[int, int], int]] = [
            ((5, 1), 1),
            ((7, 5), 1),
            ((15, 12), 3),
            ((1, 8), 1),
            ((2, 8), 2),
            ((8, 2), 2),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                x, y, d = gcdext(*args)
                assert d == want
                a, b = args
                assert a * x + b * y == d


if __name__ == "__main__":
    unittest.main()
