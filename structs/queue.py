
import unittest


class Queue(object):
    """ Queue (FIFO) implementation using lists. """

    def __init__(self):
        self.items = []

    def enqueue(self, x):
        """ Enqueues element x """
        self.items.insert(0, x)

    def dequeue(self):
        """ Dequeues element x """
        return self.items.pop()

    def peek(self):
        """ Peek next element to dequeue """
        return self.items[self.size() - 1]

    def size(self):
        """ Returns the queue size """
        return len(self.items)

    def is_empty(self):
        """ Returns True if queue is empty """
        return self.items == []


class TestQueue(unittest.TestCase):

    def test__init__(self):
        q = Queue()
        assert q.items == []

    def test_enqueue(self):
        q = Queue()
        assert q.items == []

        for x in xrange(1, 10):
            q.enqueue(x)

        assert q.items == [x for x in xrange(9, 0, -1)]

    def test_dequeue(self):
        q = Queue()
        assert q.items == []

        for x in xrange(1, 10):
            q.enqueue(x)

        assert q.items == [x for x in xrange(9, 0, -1)]

        for x in xrange(1, 10):
            e = q.dequeue()
            assert e == x

        assert q.items == []

    def test_peek(self):
        q = Queue()
        assert q.items == []

        for x in xrange(1, 10):
            q.enqueue(x)

        assert q.items == [x for x in xrange(9, 0, -1)]

        for x in xrange(1, 10):
            e = q.peek()
            assert e == x
            q.dequeue()

        assert q.items == []

    def test_size(self):
        q = Queue()
        assert q.items == []
        assert q.size() == 0

        for x in xrange(1, 10):
            q.enqueue(x)

        assert q.items == [x for x in xrange(9, 0, -1)]
        assert q.size() == 9

        for x in xrange(1, 10):
            q.dequeue()

        assert q.size() == 0

    def test_is_empty(self):
        q = Queue()
        assert q.items == []
        assert q.size() == 0
        assert q.is_empty()

        for x in xrange(1, 10):
            q.enqueue(x)

        assert q.items == [x for x in xrange(9, 0, -1)]
        assert q.size() == 9
        assert not q.is_empty()


if __name__ == "__main__":
    unittest.main(module="queue", exit=False)
