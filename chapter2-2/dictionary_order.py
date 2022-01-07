import unittest
from typing import List


def solve(s) -> str:
    """Sの先頭末尾の若いほうから削っていく"""

    r = s[::-1]

    print(s, r)
    t = ""
    for _ in range(len(s)):
        if s < r:
            t += s[0]
            s = s[1:]
        else:
            t += r[0]
            r = r[1:]

    return t


class Test(unittest.TestCase):
    def test_solve(self):
        tests = [
            ("ACDBCB", "ABCBCD"),
            ("BACB", "BABC"),
            ("BCAB", "BABC"),
        ]
        for i, (s, want) in enumerate(tests):
            with self.subTest(i):
                got = solve(s)
                self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
