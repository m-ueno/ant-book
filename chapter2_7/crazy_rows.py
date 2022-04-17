import unittest


def solve(matrix: list[list[int]]) -> int:
    n = len(matrix)
    a: list[int] = []
    count = 0
    for i in range(n):
        pos = -1
        for j in range(n - 1, -1, -1):  # j=[n-1,-1) = [n-1,0] = {n-1, ..., 0}
            if matrix[i][j] == 1:
                pos = j
                break
        a.append(pos)

    assert len(a) == n

    for i in range(n - 1):
        pos = -1
        for j in range(i, n):
            if a[j] <= i:
                pos = j
                break

        for j in range(pos, i, -1):  # j=pos, pos-1, ..., i+1
            a[j], a[j - 1] = a[j - 1], a[j]
            count += 1
    return count


class Test(unittest.TestCase):
    def test_solve(self):
        m1 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
        m2 = [
            [1, 1, 1, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
        ]
        m3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        tests = [
            (m1, 2),
            (m2, 4),
            (m3, 0),
        ]

        for i, (args, want) in enumerate(tests):
            with self.subTest(i=i):
                assert solve(args) == want


if __name__ == "__main__":
    unittest.main()
