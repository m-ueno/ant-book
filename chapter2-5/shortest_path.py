from __future__ import annotations
import unittest
from math import inf
from typing import Sequence
from heapq import heappop, heappush
from itertools import combinations
from itertools import product


V = str
E = tuple[V, V, int]  # weight


def bellman_ford(start: V, goal: V, edges: Sequence[E]) -> int | float:
    """単一始点最短路問題1

    負のコストの辺がある場合に使う
    負のコストの閉路がないことも検出できる

    計算量
    ----
    負の閉路が無ければ |E|のループを高々|V|-1回繰り返すので
        ∵最短路に含まれる辺の数 = |V|-1
    O(|V| |E|)
    """
    nodes: set[V] = set(v for s, t, _ in edges for v in [s, t])  # flatten

    # 1. initialize d
    d: dict[V, int | float] = {k: inf for k in nodes}
    d[start] = 0

    # 2. relaxing loop
    for i in range(len(nodes) - 1):  # 単に|V|-1回繰り返す
        updated = False  # 早めに終わる
        for u, v, cost in edges:
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                assert d[v] != inf
                updated = True
                print(f"i={i} d[{v}] {d[v]} := d[{u}] {d[u]} + {cost}")

            # 逆向きもたどる
            if d[u] > d[v] + cost:
                d[u] = d[v] + cost
                assert d[u] != inf
                updated = True
                print(f"i={i} d[{u}] {d[u]} := d[{v}] {d[v]} + {cost}")
        if updated is False:
            break

    return d[goal]


def dijkstra(start: V, goal: V, edges: Sequence[E]) -> int | float:
    """単一始点最短路問題2

    ダイクストラ. コストが非負の場合

    計算量
    ---
    O( |E| log|V| )
        ヒープ木の操作 log(|V|) を |E|回
        ベルマンーフォードと比べるとNodeが多くても大丈夫
    """
    # 隣接リストを整形
    adj: dict[V, list[tuple[V, int]]] = {}
    for u, v, c in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, c))
        adj[v].append((u, c))

    d = {k: inf for k in adj.keys()}
    d[start] = 0

    todo = []
    heappush(todo, (0, start))  # (startからVまでのその時点での最小値, V)

    while len(todo) > 0:
        (acc, u) = heappop(todo)
        if acc < d[u]:
            # 既に探索済みだったら飛ばす★
            # 探索済みsetで管理した方がわかりやすいが、このほうがエレガント
            continue
        if u == goal:
            return d[u]
        for v, cost in adj[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                heappush(todo, (d[v], v))

    raise RuntimeError("not found")


class Test(unittest.TestCase):
    graph = (
        ("a", "b", 2),
        ("a", "c", 5),
        ("b", "c", 4),
        ("b", "d", 6),
        ("b", "e", 10),
        ("c", "d", 2),
        ("d", "f", 1),
        ("e", "f", 3),
        ("e", "g", 5),
        ("f", "g", 9),
    )
    tests = [
        (("a", "g", graph), 16),
        (("g", "a", graph), 16),
    ]

    def test_bellman_ford(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert bellman_ford(*args) == want

    def test_search(self):
        for s, t in product("abcdefg", "abcdefg"):
            with self.subTest(s=s, t=t):
                for f, g in combinations([bellman_ford, dijkstra], 2):
                    args = (s, t, self.graph)
                    got = f(*args)
                    assert got == g(*args)
                    assert got is not inf


if __name__ == "__main__":
    unittest.main()
