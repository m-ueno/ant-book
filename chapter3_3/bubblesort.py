import tree.bit
import unittest


def solve(n: int, xs: list[int]) -> int:
    """反転数を返す"""
    ans = 0
    bit = tree.bit.BIT([0] * n)
    for j in range(n):
        ans += j - bit.sum(j)
        bit.add(xs[j], 1)
    return ans


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ((4, [3, 1, 4, 2]), 3),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
