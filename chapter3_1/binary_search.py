import unittest


def lower_bound(xs: list[int], x: int) -> int:
    """x <= xs[i]を満たす最小のiを返す（xより大きい要素がなければ右端）

    condition: x <= xi
    ------ng|ok------ -> okを返す
    """

    # めぐる式: 区間(ng, ok] を更新
    ng = -1
    ok = len(xs) - 1

    while ok - ng > 1:
        mid = (ng + ok) // 2
        if x <= xs[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def upper_bound(xs: list[int], x: int) -> int:
    """x < xs[i]を満たす最小のiを返す"""
    ng = -1
    ok = len(xs) - 1

    while ok - ng > 1:
        mid = (ng + ok) // 2
        if x < xs[mid]:
            ok = mid
        else:
            ng = mid
    return ok


class Test(unittest.TestCase):
    def test_lower_bound(self):
        tests = [
            (([1, 2, 2, 3, 3], 0), 0),
            (([1, 2, 2, 3, 3], 1), 0),
            (([1, 2, 2, 3, 3], 2), 1),
            (([1, 2, 2, 3, 3], 3), 3),
            (([1, 2, 2, 3, 3], 99), 4),
            (([1, 2, 2, 4, 5], 3), 3),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert lower_bound(*args) == want

    def test_upper_bound(self):
        tests = [
            (([1, 2, 2, 3, 3], 0), 0),
            (([1, 2, 2, 3, 3], 1), 1),
            (([1, 2, 2, 3, 3], 2), 3),
            (([1, 2, 2, 3, 3], 3), 4),
            (([1, 2, 2, 3, 3], 99), 4),
            (([1, 2, 2, 4, 5], 3), 3),
        ]
        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert upper_bound(*args) == want


if __name__ == "__main__":
    unittest.main()
