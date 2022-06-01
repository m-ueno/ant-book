import unittest
from bisect import bisect_left


def solve(
    W: int,
    H: int,
    N: int,
    X1s: list[int],
    X2s: list[int],
    Y1s: list[int],
    Y2s: list[int],
) -> int:
    # {x|x1 U x2} の前後のこしてunique
    def compress(
        x1s: list[int], x2s: list[int], w: int
    ) -> tuple[list[int], list[int], int]:
        filtered: set[int] = set()
        for x in x1s + x2s:
            for d in [-1, 0, 1]:
                if 1 <= x + d <= w:
                    filtered.add(x + d)

        # x1,x2に含まれる値とその前後が残った座標
        coord = sorted(list(filtered))

        return (
            list(map(lambda x: bisect_left(coord, x), x1s)),
            list(map(lambda x: bisect_left(coord, x), x2s)),
            len(coord),
        )

    # compress
    x1s, x2s, w = compress(X1s, X2s, W)  # 0-origin 0...w
    y1s, y2s, h = compress(Y1s, Y2s, H)

    # fill compressed field
    field = [[0] * (w) for _ in range(h)]
    for i in range(N):
        for y in range(y1s[i], y2s[i] + 1):
            for x in range(x1s[i], x2s[i] + 1):
                field[y][x] = 1

    # field南端の１行が余計なのでしみでる
    count = 0
    for y in range(h):
        for x in range(w):
            if field[y][x]:
                continue
            count += 1
            # BFS
            todo = [(x, y)]
            while len(todo) > 0:
                (xx, yy), todo = todo[-1], todo[: len(todo) - 1]
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = xx + dx, yy + dy
                    if nx < 0 or ny < 0 or nx >= w or ny >= h:
                        continue
                    if field[ny][nx]:
                        continue
                    todo.append((nx, ny))
                    field[ny][nx] = 1
    return count


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            # W,H,N,x1,x2,y1,y2
            (
                (
                    10,
                    10,
                    5,
                    [1, 1, 4, 9, 10],
                    [6, 10, 4, 9, 10],
                    [4, 8, 1, 1, 6],
                    [4, 8, 10, 5, 10],
                ),
                6,
            )
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(*args) == want


if __name__ == "__main__":
    unittest.main()
