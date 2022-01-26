import unittest


def solve(r: int, xs: list[int]) -> int:
    """貪欲法

    step1. 端の点から距離R以内の最大の点を選び+1
    step2. その点からの距離がRを超える最小の点を選び, step1繰り返し
    """
    xs = sorted(xs)
    i = 0
    n = len(xs)
    count = 0
    while i < n:
        # 1.
        j = i + 1
        while j < n and xs[j] - xs[i] <= r:
            j += 1

        # 2.
        i = j - 1
        count += 1
        while j < n and xs[j] - xs[i] <= r:
            j += 1
        i = j
    return count


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (10, [1, 7, 15, 20, 30, 50], 3),
            (1, [1, 3, 5], 3),
            (0, [10, 20, 20], 2),
            (0, [1, 1, 1, 1, 1], 1),
            (10, [70, 30, 1, 7, 15, 20, 50], 4),
        ]
        for i, (r, xs, want) in enumerate(tests):
            with self.subTest(i=i):
                got = solve(r, xs)
                self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
