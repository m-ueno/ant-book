from typing import Optional
import unittest


def loop_for_k(k, n, dirs: list[int]) -> Optional[int]:
    acc = 0
    turns = 0
    f: list[int] = [0] * (n - k + 1)
    for i in range(n - k + 1):
        if (dirs[i] + acc) % 2 == 1:
            turns += 1
            f[i] = 1
            if i - k + 1 >= 0:
                acc = acc + f[i] - f[i - k + 1]
            else:
                acc = acc + f[i]
    # check interval [n-k+1, n]
    for i in range(n - k + 1, n):
        if (acc + dirs[i]) % 2 == 1:
            return None
    return turns


def solve(n, dirs: list[int]) -> tuple[int, int]:
    """returns (k, m)"""
    min_k = -1
    min_m: int = 100000
    # min(((k, m) for k, m in ((k, loop_for_k(k, n, dirs)) for k in range(1, n)) if m is not None), key=lambda km: km[1])
    for k in range(1, n + 1):
        m = loop_for_k(k, n, dirs)
        if m is not None:
            min_k = k
            min_m = min(min_m, m)
    return (min_k, min_m)


class Test(unittest.TestCase):
    def test_solve(self):
        B, F = 1, 0
        tests = [
            ((7, [B, B, F, B, F, B, B]), (3, 3)),
            ((7, [B, B, B, B, B, B, B]), (7, 1)),
            ((7, [F, F, F, F, F, F, F]), (7, 0)),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
