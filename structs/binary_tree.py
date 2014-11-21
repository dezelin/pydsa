
import random
import unittest


class TreeNode(object):
    """ Implements Binary tree node """

    def __init__(self, k, v, p=None, l=None, r=None):
        self.parent = p
        self.left = l
        self.right = r
        self.key = k
        self.value = v

    def __iter__(self):
        if self.has_left_child():
            for x in self.left:
                yield x

        yield self.key

        if self.has_right_child():
            for x in self.right:
                yield x

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_left_child(self):
        return self.parent is not None and self.parent.left == self

    def is_right_child(self):
        return self.parent is not None and self.parent.right == self

    def is_root(self):
        return self.parent is None

    def has_both_children(self):
        return self.left is not None and self.right is not None

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class BinaryTree(object):
    """ Implements Binary tree """

    def __init__(self):
        self._root = None
        self._size = 0

    def __get__item(self, k):
        return self.get(k)

    def __iter__(self):
        return self._root.__iter__()

    def __set_item__(self, k, v):
        self.add(k, v)

    def add(self, k, v):
        if self._root is None:
            self._root = TreeNode(k, v)
        else:
            self.__add(k, v, self._root)

        self._size += 1

    def get(self, k):
        n = self.__get(k, self._root)
        if n is None:
            return None

        return n.value

    def is_empty(self):
        return self._size == 0

    def remove(self, k):
        if self._size > 1:
            n = self.__get(k, self._root)
            if n is None:
                raise KeyError()

            self.__remove(n)
            self._size -= 1
        elif self._size == 1 and self._root.value == k:
            self._root = None
            self._size = 0
        else:
            raise KeyError()

    def size(self):
        return self._size

    #
    # Private methods
    #

    def __add(self, k, v, n):
        if k < n.value:
            if n.has_left_child():
                self.__add(k, v, n.left)
            else:
                n.left = TreeNode(k, v, n)
        else:
            if n.has_right_child():
                self.__add(k, v, n.right)
            else:
                n.right = TreeNode(k, v, n)

    def __get(self, k, n):
        if n is None:
            return None

        if k < n.value:
            return self.__get(k, n.left)
        elif k > n.value:
            return self.__get(k, n.right)
        else:
            return n

    def __remove(self, k, n):
        if n.is_leaf():
            if n.is_left_child():
                n.parent.left = None
            else:
                n.parent.right = None
        elif n.has_both_children():
            succ = n.right
            while succ.has_left():
                succ = succ.left

            self.__splice_node(succ)
            n.key = succ.key
            n.value = succ.value
            self._size -= 1
        else:
            if n.has_left_child():
                if n.is_left_child():
                    n.parent.left = n.left
                    n.left.parent = n.parent
                elif n.is_right_child():
                    n.parent.right = n.left
                    n.left.parent = n.parent
                else:  # _root
                    n.key = n.left.key
                    n.value = n.left.value
                    n.left = n.left.left
                    n.right = n.right.right
            else:
                if n.is_left_child():
                    n.parent.left = n.right
                    n.right.parent = n.parent
                elif n.is_right_child():
                    n.parent.right = n.right
                    n.right.parent = n.parent
                else:  # _root
                    n.key = n.right.key
                    n.value = n.right.value
                    n.left = n.right.left
                    n.right = n.right.right

        def __splice_node(self, n):
            pass


class TestBinaryTree(unittest.TestCase):
    """ Binary tree test case """

    def test__init__(self):
        h = BinaryTree()
        assert h._root is None
        assert h._size == 0

    def test_add(self):
        for _ in xrange(100):
            h = BinaryTree()
            l = [random.randrange(1000) for _ in xrange(100)]

            assert h.size() == 0
            assert h.is_empty()

            for x in l:
                h.add(x, x)

            assert h.size() == len(l)
            assert not h.is_empty()

            for x in l:
                assert x == h.get(x)

            ll = [x for x in h]

            assert len(l) == len(ll)
            assert ll == sorted(l)

if __name__ == "__main__":
    unittest.main(module="binary_tree", exit=False)
