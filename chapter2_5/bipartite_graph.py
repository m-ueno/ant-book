from __future__ import annotations
import unittest


V = int
# E = int


def solve(n: int, adj: dict[V, list[V]]) -> bool:
    """二部グラフ判定 n~1000

    計算量
    ----
    すべての頂点・辺を1回ずつみてまわるので
    O(|V|+|E|)
    """

    def bfs(seen: list[int], todo: list[tuple[int, int]]) -> bool:
        while len(todo) > 0:
            (v, acc), todo = todo[0], todo[1:]
            past = seen[v]
            if past >= 0 and past != acc:
                return False
            seen[v] = acc

            # 隣接をキューイング
            if v in adj:
                for vv in adj[v]:
                    todo.append((vv, 1 - acc))
        return True

    #
    # 連結グラフとは限らないので全部見て回る必要がある
    seen = [-1] * n
    for i in range(n):
        if seen[i] == -1:
            todo = [(i, 0)]  # (v, 頂点iからの距離の偶奇)
            if bfs(seen, todo) is False:
                return False
    return True


class Test(unittest.TestCase):
    tests = [
        ((3, {0: [1, 2], 1: [2]}), False),
        ((4, {0: [1, 3], 1: [2], 2: [3]}), True),
        ((5, {0: [1], 2: [3, 4]}), True),
    ]

    def test_solve(self):
        for i, (args, want) in enumerate(self.tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
