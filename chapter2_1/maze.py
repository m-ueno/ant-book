import unittest
from math import inf
from typing import Optional


def solve(rows, width, height, x0, y0) -> Optional[int]:
    dist = [[inf] * width for _ in range(height)]

    dist[y0][x0] = 0
    todo = [(x0, y0)]

    while len(todo) > 0:
        (x, y), todo = todo[0], todo[1:]
        acc = dist[y][x]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx, yy = x + dx, y + dy
            if xx < 0 or yy < 0 or xx >= width or yy >= height:
                continue

            # 次の候補
            if rows[yy][xx] == "G":
                print("\n".join([str(row) for row in dist]))
                return acc + 1
            elif rows[yy][xx] == "." and dist[yy][xx] is inf:
                todo.append((xx, yy))
                dist[yy][xx] = acc + 1


class Test(unittest.TestCase):
    def test_solve(self):
        test = """#S#######.#
.......#..#
.#.##..##.#
##.##......
....#####.#
.####......
....#.####.
....#....G#"""

        rows = [[x for x in row] for row in test.split("\n")]
        got = solve(rows, len(rows[0]), len(rows), 1, 0)
        self.assertEqual(got, 23)


if __name__ == "__main__":
    unittest.main()
