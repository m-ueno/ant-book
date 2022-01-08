from __future__ import annotations
import unittest
from typing import Set, List


def solve_loop(k, xs: list[int]) -> bool:
    """再帰使わない版"""
    todo = []
    acc = 0
    i = 0
    todo: list[tuple[int, int]] = [(0, 0)]
    while len(todo) > 0:
        (i, acc), todo = todo[-1], todo[:-1]
        if acc == k:
            return True
        elif i >= len(xs) or acc > k:
            continue
        else:
            n = (i + 1, acc + xs[i])
            todo.append(n)
            todo.append((i + 1, acc))
    return False


def solve_dfs(k, xs) -> bool:
    def dfs(i, acc, k, xs: List[int]) -> bool:
        if i == len(xs):
            return acc == k

        # xs[i]を使う
        if dfs(i + 1, acc, k, xs):
            return True
        # xs[i]を使わない
        if dfs(i + 1, acc + xs[i], k, xs):
            return True
        return False

    return dfs(0, 0, k, xs)


class Test(unittest.TestCase):
    tests_ok = [
        (13, [1, 2, 4, 7]),
        (5, [1, 2, 4, 7]),
        (8, [1, 2, 4, 7]),
        (10, [1, 2, 4, 7]),
    ]
    tests_ng = [
        (15, [1, 2, 4, 7]),
    ]

    def test_all(self):
        fns = [solve_dfs, solve_loop]
        from itertools import product

        for i, (fn, (k, xs)) in enumerate(product(fns, self.tests_ok)):
            with self.subTest("ok cases", i=i):
                assert fn(k, xs)

        for i, (fn, (k, xs)) in enumerate(product(fns, self.tests_ng)):
            with self.subTest("ng cases", i=i):
                assert fn(k, xs) is False


if __name__ == "__main__":
    unittest.main()
