import unittest
from typing import Optional


class Node:
    """root, 節, 葉"""

    def __init__(self, val: int, left: Optional["Node"], right: Optional["Node"]):
        self.val: int = val
        self.left = left
        self.right = right

    def insert(self, x: int):
        if x == self.val:
            # 何もしない
            return
        elif x < self.val:
            if self.left:
                self.left.insert(x)
            else:
                self.left = Node(x, None, None)
        else:
            if self.right:
                self.right.insert(x)
            else:
                self.right = Node(x, None, None)

    def dump(self, indent=0):
        print(f"{' ' * 3 * indent}{self.val}")
        for n in [self.right, self.left]:
            n and n.dump(indent + 1)

    def find(self, x) -> bool:
        # 置き換えるのはどうする
        if self.val == x:
            return True

        for n in [self.right, self.left]:
            if n and n.find(x):
                return True

        return False

    def largest(self) -> "Node":
        if self.right:
            return self.right.largest()
        else:
            return self

    def remove_naive(self, x: int, parent: Optional["Node"]):
        if self.val == x:
            if not parent:
                raise Exception("root.remove() is forbidden")

            # 4つ場合分け
            if not (self.left or self.right):
                if parent.left == self:
                    parent.left = None
                else:
                    parent.right = None
                del self  # works?
            elif self.left is None:
                if parent.left == self:
                    parent.left = self.right
                else:
                    parent.right = self.right
                del self
            elif self.right is None:
                if parent.left == self:
                    parent.left = self.left
                else:
                    parent.right = self.left
                del self
            else:
                largest = self.left.largest()
                largest.left = self.left
                largest.right = self.right
                if parent.left == self:
                    parent.left = largest
                else:
                    parent.right = largest
                del self
        elif x < self.val:
            if self.left:
                self.left.remove_naive(x, self)
        else:
            if self.right:
                self.right.remove_naive(x, self)

    def length(self) -> int:
        acc = 1
        for n in [self.left, self.right]:
            if n:
                acc += n.length()
        return acc


class BinaryTree(Node):
    root: Optional[Node]
    pass


class Test(unittest.TestCase):
    def test_insert(self):
        xs = range(10)
        btree = BinaryTree(1, None, None)
        for x in xs:
            btree.dump()
            btree.insert(x)
        assert btree.left
        assert btree.left.val == 0
        assert btree.left.left is None
        assert btree.left.right is None
        assert btree.right
        btree.dump()

    def setUp(self):
        self.tree1 = BinaryTree(100, None, None)
        for x in range(10):
            self.tree1.insert(2 ** x)

        self.tree2 = BinaryTree(100, None, None)
        for x in range(1000):
            self.tree2.insert(1000 - x)

    def test_find(self):
        assert self.tree1.find(1)
        assert self.tree1.find(2)
        assert self.tree1.find(3) is False
        assert self.tree1.find(4)
        assert self.tree1.find(512)

    def test_largest(self):
        assert self.tree1.largest().val == 512
        assert self.tree2.largest().val == 1000

    def test_length(self):
        tree = BinaryTree(5, None, None)
        xs = [4, 6, 3, 7, 2, 8, 10]
        for i, x in enumerate(xs):
            assert tree.length() == i + 1
            tree.insert(x)

        for i, x in enumerate(xs):
            tree.remove_naive(x, None)
            l = tree.length()

    def test_remove(self):
        tree = self.tree1
        assert tree.length() == 11
        tree.remove_naive(3, None)
        assert tree.length() == 11
        tree.remove_naive(4, None)
        assert tree.length() == 10
        tree.dump()
        pass


if __name__ == "__main__":
    unittest.main()
