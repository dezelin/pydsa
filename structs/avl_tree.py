
import binary_tree
import random
import unittest


class TreeNode(binary_tree.TreeNode):
    """ Tree node for AVL tree """

    def __init__(self, k, v, p=None, l=None, r=None):
        super(self.__class__, self).__init__(k, v, p, l, r)
        self.balance = 0


class AVLTree(binary_tree.BinaryTree):
    """ AVL balanced tree implementation based on BinaryTree """

    def __init__(self):
        super(self.__class__, self).__init__()

    def add(self, k, v):
        if self._root is None:
            self._root = TreeNode(k, v)
        else:
            self.__add(k, v, self._root)

        self._size += 1

    def __add(self, k, v, n):
        if k < n.value:
            if n.has_left_child():
                self.__add(k, v, n.left)
            else:
                n.left = TreeNode(k, v, n)
                self.__update_balance(n.left)
        else:
            if n.has_right_child():
                self.__add(k, v, n.right)
            else:
                n.right = TreeNode(k, v, n)
                self.__update_balance(n.right)

    def __rebalance(self, n):
        if n is None:
            return

        if n.balance < 0:
            if n.right.balance > 0:
                self.__rotate_right(n.right)

            self.__rotate_left(n)
        elif n.balance > 0:
            if n.left.balance < 0:
                self.__rotate_left(n.left)

            self.__rotate_right(n)

    def __rotate_left(self, n):
        r = n.right
        n.right = r.left
        if r.has_left_child():
            r.left.parent = n

        r.parent = n.parent

        if n.is_root():
            self._root = r
        elif n.is_left_child():
            n.parent.left = r
        else:  # n is right child
            n.parent.right = r

        n.parent = r
        r.left = n

        n.balance = n.balance + 1 - min(0, r.balance)
        r.balance = r.balance + 1 + max(0, n.balance)

    def __rotate_right(self, n):
        r = n.left
        n.left = r.right
        if r.has_right_child():
            r.right.parent = n

        r.parent = n.parent

        if n.is_root():
            self._root = r
        elif n.is_left_child():
            n.parent.left = r
        else:  # n is right child
            n.parent.right = r

        n.parent = r
        r.right = n

        n.balance = n.balance - 1 - max(0, r.balance)
        r.balance = r.balance - 1 + min(0, n.balance)

    def __update_balance(self, n):
        if n.balance < -1 or n.balance > 1:
            self.__rebalance(n)
            return

        if n.parent is not None:
            if n.is_left_child():
                n.parent.balance += 1
            elif n.is_right_child():
                n.parent.balance -= 1

            if n.parent.balance != 0:
                self.__update_balance(n.parent)


class TestAVLTree(unittest.TestCase):
    """ Test case for AVL tree """

    def test__init__(self):
        pass

    def test_add(self):
        for _ in xrange(100):
            t = AVLTree()
            l = [random.randrange(1000) for _ in xrange(100)]

            assert t.size() == 0
            assert t.is_empty()

            for x in l:
                t.add(x, x)
                assert self.__is_balanced(t)

            assert t.size() == len(l)
            assert not t.is_empty()

            for x in l:
                assert x == t.get(x)

            ll = [x for x in t]

            assert len(l) == len(ll)
            assert ll == sorted(l)

    def __is_balanced(self, t):
        r = t._root
        return self.__is_node_balanced(r)

    def __is_node_balanced(self, n):
        if n is None:
            return True

        if n.balance < -1 or n.balance > 1:
            return False

        balanced = True
        if n.has_left_child():
            balanced = balanced and self.__is_node_balanced(n.left)
        elif n.has_right_child():
            balanced = balanced and self.__is_node_balanced(n.right)

        return balanced

if __name__ == "__main__":
    unittest.main(module="avl_tree", exit=False)
