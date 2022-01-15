from __future__ import annotations
from math import inf
import unittest
from typing import Sequence


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


class Test(unittest.TestCase):
    tests = [
        (
            (
                "a",
                "g",
                (
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
                ),
            ),
            16,
        ),
    ]

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert bellman_ford(*args) == want


if __name__ == "__main__":
    unittest.main()
