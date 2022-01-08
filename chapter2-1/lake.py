import unittest


def dfs_loop(x0, y0, rows, width, height):
    """x0,y0からはじめ、そこから繋がっている点を.に置き換える"""
    assert rows[y0][x0] == "W"

    todo = [(x0, y0)]
    rows[y0][x0] = "."
    while len(todo) > 0:
        x, y = todo.pop()
        for dx, dy in [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]:
            xx, yy = x + dx, y + dy
            if xx < 0 or yy < 0 or xx >= width or yy >= height:
                continue

            # つながってたらつぶしてstackに積む
            if rows[yy][xx] == "W":
                rows[yy][xx] = "."
                todo.append((xx, yy))


def solve(rows, width, height) -> int:
    count = 0
    for y in range(height):
        for x in range(width):
            if rows[y][x] == "W":
                dfs_loop(x, y, rows, width, height)
                count += 1
    return count


class Test(unittest.TestCase):
    def test_solve(self):
        test = """W....WW.
WW....W.
..WW..WW
......WW
......W.
..W....W
WWW....W
.W.W...W
..W....W"""

        rows = [[x for x in row] for row in test.split("\n")]
        got = solve(rows, len(rows[0]), len(rows))
        self.assertEqual(got, 3)


if __name__ == "__main__":
    unittest.main()
