
import random
import unittest


def merge_sort(list):
    if len(list) == 1:
        return

    p = len(list) / 2
    l = list[:p]
    ll = list[p:]

    merge_sort(l)
    merge_sort(ll)

    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(ll):
        if l[i] < ll[j]:
            list[k] = l[i]
            i += 1
        else:
            list[k] = ll[j]
            j += 1

        k += 1

    while i < len(l):
        list[k] = l[i]
        i += 1
        k += 1

    while j < len(ll):
        list[k] = ll[j]
        j += 1
        k += 1


def test_merge_sort():
    for _ in xrange(100):
        l = [random.randrange(0, 1001) for _ in xrange(100)]
        ll = l[:]
        merge_sort(l)
        assert l == sorted(ll)


if __name__ == "__main__":
    unittest.main(module="merge_sort", exit=False)
