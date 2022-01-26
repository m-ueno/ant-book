from typing import Any, Counter, Optional
import unittest


class Node:
    # 内部ノードと葉ノード 兼用. 節

    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

    def dump(self, level: int = 0):
        """by DFS"""

        print(f"{level}: {' '*level*3} {self.value}")
        l, r = self.left, self.right
        if r:
            r.dump(level + 1)
        if l:
            l.dump(level + 1)


def huffman(s: str) -> dict[str, str]:
    """huffman coding"""

    def isleaf(n: Node) -> bool:
        return n.left is None and n.right is None

    root = huffman_tree(s)
    root and root.dump()

    def rec(n: Optional[Node], acc) -> dict:
        if n is None:
            return {}
        elif isleaf(n):
            k, v = n.value
            return {k: acc}
        return {**rec(n.left, acc + "0"), **rec(n.right, acc + "1")}

    d = rec(root, "")
    return d


def huffman_tree(s: str) -> Optional[Node]:

    counter = Counter(s)
    counter = counter.most_common()
    counter.sort(key=lambda kv: kv[1])
    # 頻度が小さいものを2つ選び木をつくる
    # 次に小さいものを選んで木を作る

    if len(counter) == 1:
        sym, i = counter[0]
        return Node((sym, i))
    tree = None
    i = 0
    while i < len(counter):
        if tree == None:
            a, b = Node(counter[i]), Node(counter[i + 1])
            tree = Node((None, a.value[1] + b.value[1]))
            tree.left, tree.right = a, b
            i += 2
        else:
            k, v = counter[i]
            a = Node((k, v))
            b = tree
            p = Node((None, v + b.value[1]))
            if v < b.value[1]:
                left, right = a, b
            else:
                left, right = b, a
            p.left = left
            p.right = right
            tree = p
            i += 1
    return tree


class Test(unittest.TestCase):
    def test_huffman(self):
        got = huffman("abbxxccccdddddddddeeeeeeeeeeeeeeeee")
        want = {
            "e": "0",
            "c": "100",
            "x": "1010",
            "a": "10110",
            "b": "10111",
            "d": "11",
        }
        assert got == want
