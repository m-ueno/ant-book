import unittest
from itertools import product
from bisect import bisect_left, bisect_right


def hanbun(ws, vs, W) -> dict[int, int]:
    n = len(ws)
    w_v = {}  # wを超えずにつくれる価値の総和　全列挙
    todo: list[tuple[int, int, int]] = []
    todo.append((0, 0, 0))

    while len(todo) > 0:
        (i, w, v), todo = todo[-1], todo[: len(todo) - 1]
        # このアイテムを使うか使わないかの探索
        if i < n:
            todo.append((i + 1, w, v))
            if w + ws[i] <= W:
                todo.append((i + 1, w + ws[i], v + vs[i]))
            else:
                # これ以上探索しない
                continue
        else:
            if w in w_v:
                w_v[w] = max(w_v[w], v)
            else:
                w_v[w] = v

    return w_v


def solve(n, ws: list[int], vs: list[int], W: int) -> int:
    """価値の総和の最大値"""
    k = n // 2
    wv1 = hanbun(ws[:k], vs[:k], W)
    wv2 = hanbun(ws[k:], vs[k:], W)
    wv2 = list(wv2.items())
    wv2 = sorted(wv2, key=lambda wv: wv[0])  # wでソート

    # TODO: (w,v)をwでソートしても、vが単調増加とは限らない

    vmax = 0
    for w1, v1 in wv1.items():
        # W-w1をこえない最大の(w2,v2)をみつける

        # めぐる式
        ok, ng = 0, len(wv2)
        while ng - ok > 1:
            mid = (ng + ok) // 2
            ww, vv = wv2[mid]
            if ww <= W - w1:
                ok = mid
            else:
                ng = mid

        _, v2 = wv2[ok]

        # v1+v2の最大値を記憶
        vmax = max(vmax, v1 + v2)
    return vmax


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            # n, ws, vs, W
            ((4, [2, 1, 3, 2], [3, 2, 4, 2], 5), 7),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
