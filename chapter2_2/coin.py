import unittest
from typing import List


def solve(ncoins: List[int], xsum: int) -> int:
    coins = [1, 5, 10, 50, 100, 500]

    xs = list(zip(coins, ncoins))
    xs.reverse()
    count = 0
    for coin, n in xs:
        t = min(xsum // coin, n)
        xsum -= t * coin
        count += t

        # if coin * n > xsum:
        #     count += xsum // coin
        #     xsum %= coin
        # else:
        #     count += n
        #     xsum -= coin * n
    return count


class Test(unittest.TestCase):
    def test_solve(self):
        got = solve([3, 2, 1, 3, 0, 2], 620)
        self.assertEqual(got, 6)


if __name__ == "__main__":
    unittest.main()
