
import random
import unittest


def quick_sort(list):
    quick_sort_helper(list, 0, len(list) - 1)


def quick_sort_helper(list, first, last):
    if last <= first:
        return

    p = quick_sort_partition(list, first, last)
    quick_sort_helper(list, first, p - 1)
    quick_sort_helper(list, p + 1, last)


def quick_sort_partition(list, first, last):
    pv = list[first]
    l = first + 1
    r = last

    done = False
    while not done:
        while l <= r and list[l] <= pv:
            l += 1

        while r >= l and list[r] > pv:
            r -= 1

        if l > r:
            done = True
        else:
            list[l], list[r] = list[r], list[l]

    list[first], list[r] = list[r], list[first]

    return r


def test_quick_sort():
    for _ in xrange(100):
        l = [random.randrange(0, 1001) for _ in xrange(100)]
        ll = l[:]
        quick_sort(l)
        assert l == sorted(ll)

if __name__ == "__main__":
    unittest.main(module="quick_sort", exit=False)
