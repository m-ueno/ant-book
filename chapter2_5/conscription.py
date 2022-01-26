from __future__ import annotations
from collections import defaultdict
from typing import Sequence, Union
import unittest
from math import inf
from heapq import heappush, heappop

from tree import UnionFindTree

V = int
E = tuple[V, V, int]


def solve(n: int, m: int, edges: Sequence[E]) -> int:
    """
    n人の男とm人の女 全員を徴収
    n,m~1e4
    R~50000

    プリム法の解答
    全域でない場合もあるので全ノード探索する

    MSTに含まれる全コスト + 初期コスト

    初期化にO(|E|)
    探索にO(|V|log(|E|))
    """

    adj: dict[V, dict[V, int]] = {}
    nodes: set[V] = set()
    nodes.update(V(x) for x in range(n))
    nodes.update(V(y + 10000) for y in range(m))
    for u, v, w in edges:
        v = v + 10000  # 男女を区別
        if u not in adj:
            adj[u] = defaultdict(int)
        if v not in adj:
            adj[v] = defaultdict(int)

        adj[u][v] = max(adj[u][v], w)
        adj[v][u] = max(adj[v][u], w)
    del edges

    def prim(adj, start: V) -> tuple[int, set[V]]:
        """startを含むMSTを返す

        Returns: MSTの辺のコストの和, MSTに含まれるノードのset
        """
        seen = set([start])
        h: list[tuple[int, V]] = []
        for v, w in adj[start].items():
            heappush(h, (w, v))

        # mst: list[tuple[V, V, int]] = []
        cost = 0
        while h:
            w, v = heappop(h)
            if v in seen:
                continue
            seen.add(v)

            # mst.append((u, v, w))
            cost += 10000 - w

            # vの先をキューイング
            for vv, ww in adj[v].items():
                heappush(h, (ww, vv))

        return cost, seen

    seen: set[V] = set()
    acc = 0
    for start in nodes:
        if start in seen:
            continue
        elif start not in adj.keys():
            acc += 10000
            continue
        cost, searched = prim(adj, start)
        acc += cost + 10000  # 初期コスト
        seen.update(searched)
    return acc


def solve_kruskal(n: int, m: int, edges: Sequence[E]) -> int:
    # n=0..n-1
    # m=0..m-1 => n,...n+m-1
    edges = [(u, v + n, w) for u, v, w in edges]

    def kruskal(edges) -> int:
        t = UnionFindTree(n + m)
        searched = set()
        rel = 0

        # relationshipが高い=costが低い
        for u, v, w in sorted(edges, key=lambda e: e[2], reverse=True):
            if not t.same(u, v):
                t.unite(u, v)
                rel += w
                searched.add(u)
                searched.add(v)
        return rel

    return 10000 * (n + m) - kruskal(edges)  # トリッキー


# for test
def parse(s: str) -> list[tuple[int]]:
    return [tuple([int(x) for x in line.split(" ")]) for line in s.splitlines()]


class Test(unittest.TestCase):
    ex1 = """4 3 6831
1 3 4583
0 0 6592
0 1 3063
3 3 4975
1 3 2049
4 2 2104
2 2 781"""
    ex2 = """2 4 9820
3 2 6236
3 1 8864
2 4 8326
2 0 5156
2 0 1463
4 1 2439
0 4 4373
3 4 8889
2 4 3133"""

    tests = [
        ((1, 1, [(0, 0, 1), (0, 0, 9999), (0, 0, 1)]), 10001),  # 辺が2本以上あることもある
        ((5, 5, parse(ex1)), 71071),
        ((5, 5, parse(ex2)), 54223),
        ((0, 0, []), 0),
        ((1, 0, []), 10000),
        ((1, 1, []), 20000),
        ((1, 1, [(0, 0, 9999)]), 10001),
    ]

    def test_parse(self):
        got = parse(self.ex1)
        assert len(got) == 8
        assert len(got[0]) == 3

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(*args) == want

    def test_solve_kruskal(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve_kruskal(*args) == want


if __name__ == "__main__":
    unittest.main()
