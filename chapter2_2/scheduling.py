# 区間スケジューリング問題

import unittest
from typing import List


def solve(n, xs_s, xs_t) -> int:
    """終了が早いものを貪欲に選ぶ

    計算量
    ---
    n~1e5なのでO(n^2)だと厳しい
    終了時間でソートして、小さい順にsをチェック
    O(N log N)

    証明
    ----
    貪欲法が最適解であることを数学的帰納法で示す

    命題：
    "アルゴリズム1"が時刻の早い順にn番目に選んだタスクnの終了時刻t_nにおいて、
    "タスクnを選ばない最適解"が選んだタスクの総数は、アルゴリズム1を超えない

    (I) n=1のとき、命題は成り立つ.
    (II)n=kのとき命題が成り立つとすると、

    仮定より、時刻t_kにおいては貪欲法が最適.
    区間[t_k, t_{k+1}]間に, タスクk+1を選ばずに2つのタスクを終わらせる選び方があったとしても、
    時刻t_{k+1}において貪欲法を超えることはない
    3つ終わらせることはできない

    (I)(II)より命題が成り立つ
    """
    # tでソートして小さい順に選んでいくだけ
    xs = zip(xs_s, xs_t)
    xs = sorted(xs, key=lambda st: st[1])
    _, told = xs[0]
    count = 1
    for s, t in xs[1:]:
        if s <= told:
            continue
        told = t
        count += 1

    assert count <= n
    return count


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            (5, [1, 2, 4, 6, 8], [3, 5, 7, 9, 10], 3),
            (3, [1, 2, 5], [10, 4, 8], 2),
            (3, [1, 3, 5], [4, 6, 10], 2),
        ]
        for i, (n, s, t, want) in enumerate(tests):
            with self.subTest(i=i):
                got = solve(n, s, t)
                self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
