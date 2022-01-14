import unittest


class UnionFindTree:
    def __init__(self, cap: int):
        self.parent = list(range(cap))  # 親要素のidx. par[x]==xのときxは根
        self.rank = [0] * cap

    def find(self, x: int) -> int:
        """find return root node of the tree"""
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int):
        """unite trees that have member x, y"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        pass

    def same(self, x: int, y: int) -> bool:
        """same return true if x and y in a tree"""
        return self.find(x) == self.find(y)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tree1 = UnionFindTree(10)
        s1 = [0, 1, 2]
        s2 = [7, 8, 9]
        for x in s1:
            self.tree1.unite(s1[0], x)
        for x in s2:
            self.tree1.unite(s2[0], x)

    def test_same(self):
        assert self.tree1.same(0, 1)
        assert self.tree1.same(1, 2)
        assert self.tree1.same(7, 9)

        # before unite
        assert self.tree1.same(0, 9) == False

        # after unite
        self.tree1.unite(0, 7)
        assert self.tree1.same(0, 8) == True


if __name__ == "__main__":
    unittest.main()
