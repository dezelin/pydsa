
import random
import unittest


def shell_sort(list):
    subl_count = len(list) / 2
    while subl_count > 0:
        for i in xrange(subl_count):
            shell_gap_sort(list, i, subl_count)

        subl_count /= 2


def shell_gap_sort(list, start, gap):
    for i in xrange(start + gap, len(list), gap):
        j = i
        p = list[i]
        while j > 0 and list[j - gap] > p:
            list[j] = list[j - gap]
            j -= gap

        list[j] = p


def test_shell_sort():
    for _ in xrange(0, 100):
        l = [random.randrange(0, 1001) for _ in xrange(100)]
        ll = l[:]
        shell_sort(ll)
        assert ll == sorted(l)


if __name__ == "__main__":
    unittest.main(module="shell_sort", exit=False)
