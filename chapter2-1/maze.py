import unittest
from math import inf
from typing import Optional

# dfsすればいい

testinput = """#S#######.#
.......#..#
.#.##..##.#
##.##......
....#####.#
.####......
....#.####.
....#....G#"""


# def solve(x0: int, y0: int, rows, width, height) -> int:
#     """必要な最小のターン数を返す"""
#     visiting = set()
#     visiting.add((x0, y0))
#     todo = [(x0, y0, 0)]

#     while len(todo) > 0:
#         (x, y, acc), todo = todo[0], todo[1:]

#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

#             print(len(visiting))

#             xx, yy = x + dx, y + dy
#             if xx < 0 or yy < 0 or xx >= width or yy >= height:
#                 continue

#             # 次の候補
#             if rows[yy][xx] == "G":
#                 return acc + 1
#             elif rows[yy][xx] == "." and (xx, yy) not in visiting:
#                 todo.append((xx, yy, acc + 1))
#                 visiting.add((xx, yy))

#     raise RuntimeError("goal not found")


def solve(rows, width, height, x0, y0) -> Optional[int]:
    dist = []
    for _ in range(height):
        dist.append([inf] * width)
    assert len(dist) == height

    todo = [(x0, y0)]
    dist[y0][x0] = 0

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
        rows = [[x for x in row] for row in testinput.split("\n")]
        got = solve(rows, len(rows[0]), len(rows), 1, 0)
        self.assertEqual(got, 23)


if __name__ == "__main__":
    unittest.main()
