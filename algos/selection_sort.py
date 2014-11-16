
import random
import unittest


def selection_sort(list):
    for i in xrange(len(list) - 1, 0, -1):
        m = 0
        for j in xrange(1, i + 1):
            if list[m] < list[j]:
                m = j

        list[m], list[i] = list[i], list[m]


def test_selection_sort():
    for _ in xrange(0, 100):
        l = [random.randrange(0, 1001) for _ in xrange(100)]
        ll = l[:]
        selection_sort(ll)
        assert ll == sorted(l)


if __name__ == "__main__":
    unittest.main(module="selection_sort", exit=False)
