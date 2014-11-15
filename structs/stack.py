
import unittest


class Stack(object):
    """
    Stack data structure implementation using built-in list.
    """

    def __init__(self):
        """ Constructor """
        self.items = []

    def push(self, x):
        """ Pushes element x on top of the stack """
        self.items.append(x)

    def pop(self):
        """ Pops the element from the top """
        return self.items.pop()

    def peek(self):
        """ Peek next element """
        return self.items[self.size() - 1]

    def size(self):
        """ Returns the size of the stack """
        return len(self.items)

    def is_empty(self):
        """ Returns True if the stack is empty """
        return self.size() == 0


class TestStack(unittest.TestCase):

    def test__init__(self):
        stack = Stack()
        assert stack.items == []

    def test_push(self):
        stack = Stack()
        assert len(stack.items) == 0
        for i in xrange(1, 10):
            stack.push(i)
            assert len(stack.items) == i
            assert stack.items[i - 1] == i

        assert stack.items == [i for i in xrange(1, 10)]

    def test_pop(self):
        stack = Stack()
        assert len(stack.items) == 0
        for i in xrange(1, 10):
            stack.push(i)
            assert len(stack.items) == i

        assert stack.items == [i for i in xrange(1, 10)]

        for i in xrange(9, 0, -1):
            x = stack.pop()
            assert x == i

        assert stack.items == []

    def test_peek(self):
        s = Stack()
        assert s.items == []

        for i in xrange(1, 10):
            s.push(i)

        assert s.items == [i for i in xrange(1, 10)]

        for i in xrange(9, 0, -1):
            assert s.peek() == s.pop()

        assert s.items == []

    def test_size(self):
        stack = Stack()
        assert stack.size() == 0
        for i in xrange(1, 10):
            stack.push(i)
            assert stack.size() == i

        assert stack.items == [i for i in xrange(1, 10)]

    def test_is_empty(self):
        stack = Stack()
        assert stack.is_empty()
        for i in xrange(1, 10):
            stack.push(i)
            assert not stack.is_empty()

        assert stack.items == [i for i in xrange(1, 10)]

if __name__ == "__main__":
    unittest.main(module="stack", exit=False)
