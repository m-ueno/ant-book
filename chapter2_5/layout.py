from __future__ import annotations
from collections import defaultdict
from typing import Sequence, Union
import unittest
from math import inf
from heapq import heappush, heappop

from tree import UnionFindTree

V = int
E = tuple[V, V, int]


def solve(n: int, likes, dislikes) -> int:
    # 牛は番号順に並んでいる
    # d[i]
    # likes: (a,b,最大距離) * ML
    # dis : (a,b, 最小距離) * MD
    # 制約を満たす1番目とN番目の牛の間の最大距離
    # d[i] <= d[i+1]
    # d[b] - dl <= d[a]
    # d[b] - dd >= d[a]

    # グラフの最短路
    # 辺e = (v, u)に対して
    # d[v]+w >= d[u]
    #   vまでの最短路とeを経由してuに向かう >= vへの最短距離
    
    # ほしいのはd[N]-d[1]の最大値
    # 不等式を満たす最大値は、vへの最短パスに対応（？？？）
    # 
    return acc


class Test(unittest.TestCase):
    tests = []

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
