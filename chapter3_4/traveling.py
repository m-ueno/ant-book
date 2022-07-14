import unittest
from collections import defaultdict, namedtuple
from itertools import chain, combinations
from math import inf

Graph = list[tuple[int, int, int]]


def solve(g: Graph, n, m, a: int, b, t: list[int]) -> int:
    # n枚、m都市

    # 引数が1originで与えられるので0originに
    a = a - 1
    b = b - 1
    # 距離行列
    d = [[inf] * m for _ in range(m)]
    for i, j, w in g:
        d[i - 1][j - 1] = w
        d[j - 1][i - 1] = w

    # 状態ノード: 残りの乗車券, 現在位置v, vに至る最短時間 の3-tuple
    Node = namedtuple("Node", ["current", "remain_tickets", "time"])

    # 残りn枚
    remains_all = frozenset(range(n))

    # dp[S, v] : (残っている乗車券がS, 現在位置がv)という状態に至るまでの最短時間
    dp: dict[tuple[frozenset[int], int], float] = defaultdict(lambda *args: inf)
    dp[remains_all, a] = 0  # 1枚も使わずにaにいる

    # BFSで全探索しながらdpテーブルを埋めていく
    todo = [Node(a, remains_all, 0)]
    while len(todo) > 0:
        node, todo = todo[0], todo[1:]
        v = node.current
        for i in node.remain_tickets:  # 次使うチケット
            horse_power = t[i]
            for u in range(m):  # 次の都市
                remain_next = node.remain_tickets - {i}
                time_next = node.time + d[v][u] / horse_power
                todo.append(Node(u, remain_next, time_next))
                dp[remain_next, u] = min(dp[remain_next, u], time_next)

    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    # bに至る最短時間をえる
    # どのチケットが余るかわからないので全部なめる
    # ビットDPで書いておくとべき集合なめるのを綺麗に書ける
    ans = inf
    for remain in powerset(remains_all):
        s = frozenset(remain)
        ans = min(ans, dp[s, b])

    return ans


class Test(unittest.TestCase):
    def test_solve(self):
        g = [
            (1, 3, 3),
            (1, 4, 2),
            (2, 3, 3),
            (2, 4, 5),
        ]

        tests = [
            ((g, 2, 4, 1, 1, [3, 1]), 0),
            ((g, 2, 4, 2, 1, [3, 1]), 5 / 3.0 + 2.0),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
