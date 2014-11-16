
import random
import unittest


def insertion_sort(list):
    for i in xrange(1, len(list)):
        j = i
        p = list[i]
        while j > 0 and list[j - 1] > p:
            list[j] = list[j - 1]
            j -= 1

        list[j] = p


def test_insertion_sort():
    for _ in xrange(0, 100):
        l = [random.randrange(0, 1001) for _ in xrange(100)]
        ll = l[:]
        insertion_sort(ll)
        assert ll == sorted(l)


if __name__ == "__main__":
    unittest.main(module="insertion_sort", exit=False)
