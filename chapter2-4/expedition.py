from __future__ import annotations
import unittest
from heapq import heappush, heappop


def solve(n: int, L: int, P: int, a: list[int], b: list[int]) -> int:
    acc = 0
    x = 0  # current pos
    h = []

    # *Append goal*
    a.append(L)
    b.append(0)

    for i in range(n + 1):
        d = a[i] - x
        while P - d < 0:  # ガソリンが空でなくなるまで補給を繰り返す
            if len(h) == 0:
                return -1
            P -= heappop(h)
            acc += 1

        P -= d
        assert P >= 0

        x = a[i]
        heappush(h, -b[i])

    return acc


# def solve_ng(n: int, L: int, P: int, xs_a: list[int], xs_b: list[int]) -> int:
#     """ガソリンの補給回数の最小値 できない場合は-1

#     計算量
#     ----
#     O(n*logn)
#         各スタンドを調べるのは高々1回だけ
#     """
#     acc = 0
#     x = 0  # 現在地
#     i = 0  # 次のGS idx
#     while x < L:
#         if L <= x + P:
#             return acc

#         h = []

#         for j in range(i, n):
#             if xs_a[j] <= x + P:
#                 heappush(h, -xs_b[j])
#             else:
#                 break

#         # (2)
#         if len(h) == 0:
#             return -1

#         # ガス欠地点は[j, j+1)の間
#         x = x + P
#         maxb = -heappop(h)
#         P = maxb
#         if i < j:
#             i = j
#         else:
#             return -1
#         acc += 1

#     return acc


class Test(unittest.TestCase):
    tests = [
        ((4, 25, 10, [10, 14, 20, 21], [10, 5, 2, 4]), 2),  # n,L,P,ai,bi
        ((1, 100, 10, [99], [1000]), -1),
        ((2, 150, 50, [50, 100], [50, 51]), 2),
        ((2, 150, 50, [50, 100], [50, 50]), 2),
        ((2, 150, 50, [50, 100], [50, 49]), -1),
    ]

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
