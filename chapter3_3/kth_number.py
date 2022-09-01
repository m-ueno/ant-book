import unittest
from math import sqrt, ceil
from bisect import bisect_right


def solve_naive(
    n: int, m: int, xs: list[int], queries: list[tuple[int, int, int]]
) -> list[int]:
    # 入力のi,j,kは1-originだからそれぞれ-1する
    # 入力のi,jは閉区間[i,j]だからjは+1する
    return [sorted(xs[i - 1 : j])[k - 1] for i, j, k in queries]


def count_bucket(bucket: list[int], x: int) -> int:
    """ソート済みリストの、x以下の要素数を返す"""
    ok, ng = 0, len(bucket)

    def is_ok(i: int) -> bool:
        return bucket[i] <= x

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok + 1  # upper boundを要素数に


def solve(
    n: int, m: int, xs: list[int], queries: list[tuple[int, int, int]]
) -> list[int]:
    # 平方分割
    B = ceil(sqrt(n))
    # https://stackoverflow.com/a/434328
    chunks = [xs[pos : pos + B] for pos in range(0, n, B)]

    # nums: xs全体のソート済みリスト
    nums = sorted(xs)

    # 各分割をソート
    chunks = [sorted(chunk) for chunk in chunks]

    # 区間[i, j]のx以下の要素数を数える
    # = 区間[l, r)のx以下の要素数を数える
    # x以下の要素数が、k以上ならtrueを返す
    def is_ok(i: int, j: int, k: int, x: int) -> int:
        count = 0
        l = i - 1
        r = j
        # https://aotamasaki.hatenablog.com/entry/ants_book_part2#P168-K-th-Number
        l_bucket = (l - 1) // B + 1
        r_bucket = r // B

        if True:
            count += sum((xx <= x for xx in xs[l : l_bucket * B]))
            count += sum((xx <= x for xx in xs[r_bucket * B : r]))
            # =>  [2,1,1]
            # なんかかわったが、どのみち間違い
        else:
            # => [3,1,1]
            # バケットをはみ出す部分
            while l < r and l % B != 0:
                if xs[l] <= x:
                    count += 1
                l += 1
            while l < r - 1 and (r - 1) % B != 0:  # r未満の最大
                if xs[r - 1] <= x:
                    count += 1
                r -= 1

        # バケットごとの二部探索
        while l < r: # TODO
            chunk = chunks[l // B]
            # count += count_bucket(chunk, x)  # bisect_rightでok
            count += bisect_right(chunk, x)
            l += B
        return count >= k

    kth_numbers = []
    for i, j, k in queries:
        ng, ok = -1, n - 1  # (ng, ok]
        # xについて二部探索
        # ok: 値がnums[ok]以下の要素数がk以上である

        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            x = nums[mid]
            if is_ok(i, j, k, x):
                ok = mid
            else:
                ng = mid

        kth_numbers.append(nums[ok])
    return kth_numbers


def solve_seg(
    n: int, m: int, xs: list[int], queries: list[tuple[int, int, int]]
) -> list[int]:
    pass


class Test(unittest.TestCase):
    def test_count_bucket(self):
        a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
        tests = [
            ((a, 1), 2),
            ((a, 2), 4),
            ((a, 5), len(a)),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert count_bucket(*args) == want

    def test_solve_naive(self):
        tests = [
            # n,m,a,query
            (
                (7, 3, [1, 5, 2, 6, 3, 7, 4], [(2, 5, 3), (4, 4, 1), (1, 7, 3)]),
                [5, 6, 3],
            ),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve_naive(*args) == want

    def test_solve(self):
        tests = [
            # n,m,a,query
            (
                (7, 3, [1, 5, 2, 6, 3, 7, 4], [(2, 5, 3), (4, 4, 1), (1, 7, 3)]),
                [5, 6, 3],
            ),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve_naive(*args) == solve(*args)


if __name__ == "__main__":
    unittest.main()
