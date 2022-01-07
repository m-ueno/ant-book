import unittest
from typing import Set, List


# def dfs(k, partial_sum: int, seen: Set[int], todo: Set[int]) -> bool:
#     if partial_sum == k:
#         return True

#     for x in todo:
#         if dfs(k, partial_sum + x, seen | set([x]), todo - set([x])):
#             return True

#     return False


# def solve(k, xs) -> bool:
#     return dfs(k, 0, set(), set(xs))


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


def solve(k, xs) -> bool:
    return dfs(0, 0, k, xs)


class Test(unittest.TestCase):
    def test_true(self):
        tests = [
            (13, [1, 2, 4, 7]),
            (5, [1, 2, 4, 7]),
            (8, [1, 2, 4, 7]),
            (10, [1, 2, 4, 7]),
        ]
        for k, xs in tests:
            self.assertTrue(solve(k, xs))

    def test_false(self):
        k, xs = 15, [1, 2, 4, 7]
        self.assertFalse(solve(k, xs))


if __name__ == "__main__":
    unittest.main()
