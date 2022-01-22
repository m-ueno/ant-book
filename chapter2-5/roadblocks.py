from __future__ import annotations
from collections import defaultdict
from typing import Sequence
import unittest
from math import inf
from heapq import heappush, heappop

V = int
E = tuple[V, V, int]


def solve(start: V, goal: V, edges: Sequence[E]) -> int | float:
    """二番目の最短路

    N個のノード N~5e3
    R本のエッジ R~1e6

    bellman-fordは O(|V||E|)~5e9 計算量ギリギリ

    vへの2番目の最短路はいずれか：
    - uへの最短路にu->vの辺をつなげたもの
        - 普通のダイクストラ法
    - uへの2番目の最短路にu->vの辺をつなげたもの
    updateがある限り続ける
    """

    adj: dict[V, list[tuple[V, int]]] = {}
    for s, t, cost in edges:
        if s not in adj:
            adj[s] = []
        if t not in adj:
            adj[t] = []
        adj[s].append((t, cost))
        adj[t].append((s, cost))

    dist: dict[V, int | float] = defaultdict(lambda *args: inf)
    dist2: dict[V, int | float] = defaultdict(lambda *args: inf)

    dist[start] = 0
    h: list[tuple[int | float, V]] = []
    heappush(h, (0, start))

    while h:
        d, u = heappop(h)
        if dist2[u] < d:  # avoid infinite loop
            continue

        for v, cost in adj[u]:
            d1 = d + cost
            d2 = dist2[u] + cost

            # ifの中で選ぶとsortをなくせる気がするが
            # ラクをしている
            d1, d2 = sorted([dist[v], dist2[v], d1, d2])[:2]

            if d1 < dist[v]:
                dist[v] = d1
                dist2[v] = d2
                heappush(h, (d1, v))

            if d2 < dist2[v]:
                dist2[v] = d2
                heappush(h, (d2, v))

    return dist2[goal]


class Test(unittest.TestCase):
    graph = (  # N,R=4,4
        (1, 2, 100),
        (2, 3, 250),
        (2, 4, 200),
        (3, 4, 100),
    )
    tests = [
        ((1, 4, graph), 450),
    ]

    def test_solve(self):
        args, want = self.tests[0]
        assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
