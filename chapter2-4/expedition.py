from __future__ import annotations
import unittest
from heapq import heappush, heappop


def solve(n: int, L: int, P: int, xs_a: list[int], xs_b: list[int]) -> int:
    """ガソリンの補給回数の最小値 できない場合は-1

    n~10000

    燃料が0になったときに最大のAiで補給していたことにする
                   A   B
        a: 0.......40...50.........90
        b: 0.......101..100........x
        P=90
        座標90で0になる
        Aで補給後：90-40+101 = 151
            このままBにつくと 141
        Bで補給後：90-50+100 = 140
        Aで補給した方がいい

    計算量
    ----
    O(n*logn)
        各スタンドを調べるのは高々1回だけ

    """
    acc = 0
    x = 0  # 現在地
    i = 0  # 次のGS idx
    while i < n:
        h = []
        j = i
        for j in range(i, n):
            if P < xs_a[j] - x:
                break
            else:
                # 記憶して通過
                # 符号反転
                heappush(h, -xs_b[j])

        if len(h) == 0:
            return -1

        # ガス欠地点はjとj+1の間
        x = x + P
        maxb = -heappop(h)
        P = maxb
        i = j + 1
        acc += 1

    # ぴったりたどりつくかどうか

    return acc


class Test(unittest.TestCase):
    tests = [
        ((4, 25, 10, [10, 14, 20, 21], [10, 5, 2, 4]), 2),  # n,L,P,ai,bi
        ((1, 100, 10, [99], [1000]), -1),
        ((2, 150, 50, [50, 100], [50, 50]), 2),  # n,L,P,ai,bi
    ]

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
