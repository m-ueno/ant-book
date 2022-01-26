from __future__ import annotations
from typing import Sequence
import unittest
from math import inf
from heapq import heappush, heappop
import sys

from union_find_tree import UnionFindTree

# from tree import UnionFindTree

V = int
E = tuple[V, V, int]


def prim(edges: Sequence[E]) -> int:
    """プリム法

    計算量
    ---
    O(|E|log(|V|))

    貪欲法の証明は、最小コストの辺e: u->v を加えると閉路ができると仮定して背理法

    V
        集合X
            全域木T
                最小全域木が存在
    隣接エッジコストをpush
        (u,v, cost)をpush  u∈X, v∈V-X
    (u,v,cost)をpop
    """
    adj: dict[V, dict[V, int]] = {}
    for u, v, w in edges:
        if u not in adj:
            adj[u] = {}
        if v not in adj:
            adj[v] = {}
        adj[u][v] = w
        adj[v][u] = w

    nodes: set[V] = set([x for s, t, _ in edges for x in (s, t)])
    start = nodes.pop()
    seen: set[V] = set([start])

    h: list[tuple[int, tuple[V, V]]] = []
    for v, w in adj[start].items():
        heappush(h, (w, (start, v)))  # 最小の辺だけでいいのでは あとで最小になるかもしれない

    mst = []
    while h:
        w, (u, v) = heappop(h)

        # uがXに、vがV\xに含まれていればMSTの辺が確定
        # 取り出すとき確定
        # （pushするときではない）
        if v in seen or u not in seen:
            continue
        seen.add(v)
        mst.append((u, v, w))

        # vの先を探索
        for vv, ww in adj[v].items():
            heappush(h, (ww, (v, vv)))
    return sum(w for _, _, w in mst)


def kruskal(edges: Sequence[E]) -> int:
    """最小全域森を求める. 森の辺の重みの総和を返す

    プリム法と違って全域でなくても大丈夫

    辺が小さい順に
    - 辺eが閉路をつくらないなら、MSTに加える
        - 両端がどちらも既存のTreeでなければあらたにTreeを追加
    - つくるなら不要なのでスキップ

    UnionFind木でのUnionが1つのMSTに対応する
    """
    edges = sorted(edges, key=lambda x: x[2])
    nodes: set[V] = set([x for s, t, w in edges for x in [s, t]])
    t = UnionFindTree(len(nodes)+1)
    cost = 0
    for u, v, w in edges:
        if not t.same(u, v):
            t.unite(u, v)
            cost += w
    return cost


class Test(unittest.TestCase):
    graph = (  # N,R=4,4
        (1, 2, 100),
        (2, 3, 250),
        (2, 4, 200),
        (3, 4, 100),
    )
    graph_star = (
        (1, 2, 10),
        (1, 3, 10),
        (1, 4, 10),
        (1, 5, 10),
    )
    tests = [
        (graph, 400),
        (graph_star, 40),
    ]

    def test_prim(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert prim(args) == want

    def test_kruskal(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert kruskal(args) == want


if __name__ == "__main__":
    unittest.main()
