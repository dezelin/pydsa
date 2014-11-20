
import random
import unittest


class BinaryHeap(object):
    """ Binary heap implementation using Python list """

    def __init__(self):
        self.__heap = [0]
        self.__size = 0

    def __perc_up(self, i):
        while i // 2 > 0:
            if self.__heap[i] < self.__heap[i // 2]:
                self.__heap[i], self.__heap[i // 2] = self.__heap[i // 2], \
                    self.__heap[i]
            i //= 2

    def __perc_down(self, i):
        while i * 2 <= self.__size:
            j = self.__find_min_child(i)
            if self.__heap[i] > self.__heap[j]:
                self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

            i = j

    def __find_min_child(self, i):
        if i * 2 + 1 > self.__size:
            return i * 2
        else:
            if self.__heap[i * 2] < self.__heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, k):
        self.__heap.append(k)
        self.__size += 1
        self.__perc_up(self.__size)

    def del_min(self):
        tmp = self.__heap[1]
        self.__heap[1] = self.__heap[self.__size]
        self.__size -= 1
        self.__heap.pop()
        self.__perc_down(1)
        return tmp

    def size(self):
        return self.__size

    def is_empty(self):
        return self.size() == 0


class TestBinaryHeap(unittest.TestCase):
    def test__init__(self):
        h = BinaryHeap()
        assert h._BinaryHeap__heap == [0]
        assert h._BinaryHeap__size == 0

    def test_insert(self):
        for _ in xrange(100):
            h = BinaryHeap()
            l = [random.randrange(1000) for _ in xrange(100)]
            for x in l:
                h.insert(x)

            assert self.__is_complete(h)

    def test_del_min(self):
        self.test_is_empty()

    def test_size(self):
        self.test_is_empty()

    def test_is_empty(self):
        for _ in xrange(100):
            h = BinaryHeap()
            l = [random.randrange(1001) for _ in xrange(100)]
            for x in l:
                h.insert(x)

            assert h.size() == 100
            assert not h.is_empty()

            for _ in xrange(100):
                h.del_min()

            assert h.size() == 0
            assert h.is_empty()

    def __is_complete(self, h):
        l = []
        while not h.is_empty():
            l.append(h.del_min())

        ll = l[:]
        return l == sorted(ll)


if __name__ == "__main__":
    unittest.main(module="binary_heap", exit=False)
