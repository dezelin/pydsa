
import unittest


class Dequeue(object):
    """ Dequeu implementation using list """

    def __init__(self):
        """ Constructor """
        self.items = []

    def add_front(self, x):
        """ Adds element x to the front of dequeue """
        self.items.append(x)

    def pop_front(self):
        """ Pops first element from the front of dequeue """
        return self.items.pop()

    def peek_front(self):
        """ Peeks first element at the front of dequeue """
        return self.items[self.size() - 1]

    def add_back(self, x):
        """ Adds element x to the back of dequeue """
        self.items.insert(0, x)

    def pop_back(self):
        """ Pops first element from the back of dequeue """
        return self.items.pop(0)

    def peek_back(self):
        """ Peeks first element at the back of dequeue """
        return self.items[0]

    def size(self):
        """ Returns the number of elements in dequeue """
        return len(self.items)

    def is_empty(self):
        """ Returns True if dequeue is empty """
        return self.items == []


class TestDequeue(unittest.TestCase):

    def test__init__(self):
        d = Dequeue()
        assert d.items == []
        assert len(d.items) == 0
        assert d.size() == 0

    def test_add_front(self):
        d = Dequeue()
        assert d.items == []

        for x in xrange(1, 10):
            d.add_front(x)

        assert d.items == [i for i in xrange(1, 10)]

    def test_pop_front(self):
        d = Dequeue()
        assert d.items == []

        for x in xrange(1, 10):
            d.add_front(x)

        assert d.items == [i for i in xrange(1, 10)]

        for x in xrange(9, 0, -1):
            assert x == d.pop_front()

        assert d.items == []

    def test_peek_front(self):
        d = Dequeue()
        assert d.items == []

        for x in xrange(1, 10):
            d.add_front(x)

        assert d.items == [i for i in xrange(1, 10)]

        for x in xrange(9, 0, -1):
            assert d.peek_front() == d.pop_front()

        assert d.items == []

    def test_add_back(self):
        d = Dequeue()
        assert d.items == []

        for x in xrange(1, 10):
            d.add_back(x)

        assert d.items == [i for i in xrange(9, 0, -1)]

    def test_pop_back(self):
        d = Dequeue()
        assert d.items == []

        for x in xrange(1, 10):
            d.add_back(x)

        assert d.items == [i for i in xrange(9, 0, -1)]

        for x in xrange(9, 0, -1):
            assert x == d.pop_back()

        assert d.items == []

    def test_peek_back(self):
        d = Dequeue()
        assert d.items == []

        for x in xrange(1, 10):
            d.add_back(x)

        assert d.items == [i for i in xrange(9, 0, -1)]

        for x in xrange(9, 0, -1):
            assert d.peek_back() == d.pop_back()

        assert d.items == []


if __name__ == "__main__":
    unittest.main(module="dequeue", exit=False)
