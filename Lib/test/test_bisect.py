import unittest
from test import test_support
from bisect import bisect_right, bisect_left, insort_left, insort_right

# XXX optional slice arguments need tests.


class TestBisect(unittest.TestCase):

    precomputedCases = [
        (bisect_right, [], 1, 0),
        (bisect_right, [1], 0, 0),
        (bisect_right, [1], 1, 1),
        (bisect_right, [1], 2, 1),
        (bisect_right, [1, 1], 0, 0),
        (bisect_right, [1, 1], 1, 2),
        (bisect_right, [1, 1], 2, 2),
        (bisect_right, [1, 1, 1], 0, 0),
        (bisect_right, [1, 1, 1], 1, 3),
        (bisect_right, [1, 1, 1], 2, 3),
        (bisect_right, [1, 1, 1, 1], 0, 0),
        (bisect_right, [1, 1, 1, 1], 1, 4),
        (bisect_right, [1, 1, 1, 1], 2, 4),
        (bisect_right, [1, 2], 0, 0),
        (bisect_right, [1, 2], 1, 1),
        (bisect_right, [1, 2], 1.5, 1),
        (bisect_right, [1, 2], 2, 2),
        (bisect_right, [1, 2], 3, 2),
        (bisect_right, [1, 1, 2, 2], 0, 0),
        (bisect_right, [1, 1, 2, 2], 1, 2),
        (bisect_right, [1, 1, 2, 2], 1.5, 2),
        (bisect_right, [1, 1, 2, 2], 2, 4),
        (bisect_right, [1, 1, 2, 2], 3, 4),
        (bisect_right, [1, 2, 3], 0, 0),
        (bisect_right, [1, 2, 3], 1, 1),
        (bisect_right, [1, 2, 3], 1.5, 1),
        (bisect_right, [1, 2, 3], 2, 2),
        (bisect_right, [1, 2, 3], 2.5, 2),
        (bisect_right, [1, 2, 3], 3, 3),
        (bisect_right, [1, 2, 3], 4, 3),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 0, 0),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 1, 1),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 1.5, 1),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2, 3),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2.5, 3),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3, 6),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3.5, 6),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4, 10),
        (bisect_right, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 5, 10),

        (bisect_left, [], 1, 0),
        (bisect_left, [1], 0, 0),
        (bisect_left, [1], 1, 0),
        (bisect_left, [1], 2, 1),
        (bisect_left, [1, 1], 0, 0),
        (bisect_left, [1, 1], 1, 0),
        (bisect_left, [1, 1], 2, 2),
        (bisect_left, [1, 1, 1], 0, 0),
        (bisect_left, [1, 1, 1], 1, 0),
        (bisect_left, [1, 1, 1], 2, 3),
        (bisect_left, [1, 1, 1, 1], 0, 0),
        (bisect_left, [1, 1, 1, 1], 1, 0),
        (bisect_left, [1, 1, 1, 1], 2, 4),
        (bisect_left, [1, 2], 0, 0),
        (bisect_left, [1, 2], 1, 0),
        (bisect_left, [1, 2], 1.5, 1),
        (bisect_left, [1, 2], 2, 1),
        (bisect_left, [1, 2], 3, 2),
        (bisect_left, [1, 1, 2, 2], 0, 0),
        (bisect_left, [1, 1, 2, 2], 1, 0),
        (bisect_left, [1, 1, 2, 2], 1.5, 2),
        (bisect_left, [1, 1, 2, 2], 2, 2),
        (bisect_left, [1, 1, 2, 2], 3, 4),
        (bisect_left, [1, 2, 3], 0, 0),
        (bisect_left, [1, 2, 3], 1, 0),
        (bisect_left, [1, 2, 3], 1.5, 1),
        (bisect_left, [1, 2, 3], 2, 1),
        (bisect_left, [1, 2, 3], 2.5, 2),
        (bisect_left, [1, 2, 3], 3, 2),
        (bisect_left, [1, 2, 3], 4, 3),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 0, 0),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 1, 0),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 1.5, 1),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2, 1),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2.5, 3),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3, 3),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3.5, 6),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4, 6),
        (bisect_left, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 5, 10)
    ]

    def test_precomputed(self):
        for func, list, elt, expected in self.precomputedCases:
            self.assertEqual(func(list, elt), expected)

    def test_random(self, n=20):
        from random import randrange
        for i in xrange(n):
            data = [randrange(0, n, 2) for j in xrange(i)]
            data.sort()
            elem = randrange(n)
            ip = bisect_left(data, elem)
            if ip < len(data):
                self.failUnless(elem <= data[ip])
            if ip > 0:
                self.failUnless(data[ip-1] < elem)
            ip = bisect_right(data, elem)
            if ip < len(data):
                self.failUnless(elem < data[ip])
            if ip > 0:
                self.failUnless(data[ip-1] <= elem)

#==============================================================================

class TestInsort(unittest.TestCase):

    def test_vsListSort(self, n=500):
        from random import choice
        digits = "0123456789"
        raw = []
        insorted = []
        for i in range(n):
            digit = choice(digits)
            raw.append(digit)
            if digit in "02468":
                f = insort_left
            else:
                f = insort_right
            f(insorted, digit)
        sorted = raw[:]
        sorted.sort()
        self.assertEqual(sorted, insorted)

#==============================================================================

libreftest = """
Example from the Library Reference:  Doc/lib/libbisect.tex

The bisect() function is generally useful for categorizing numeric data.
This example uses bisect() to look up a letter grade for an exam total
(say) based on a set of ordered numeric breakpoints: 85 and up is an `A',
75..84 is a `B', etc.

    >>> grades = "FEDCBA"
    >>> breakpoints = [30, 44, 66, 75, 85]
    >>> from bisect import bisect
    >>> def grade(total):
    ...           return grades[bisect(breakpoints, total)]
    ...
    >>> grade(66)
    'C'
    >>> map(grade, [33, 99, 77, 44, 12, 88])
    ['E', 'A', 'B', 'D', 'F', 'A']

The bisect module can be used with the Queue module to implement
a priority queue (example courtesy of Fredrik Lundh):

>>> import Queue, bisect
>>> class PriorityQueue(Queue.Queue):
...     def _put(self, item):
...         bisect.insort(self.queue, item)
...
>>> queue = PriorityQueue(0)
>>> queue.put((2, "second"))
>>> queue.put((1, "first"))
>>> queue.put((3, "third"))
>>> queue.get()
(1, 'first')
>>> queue.get()
(2, 'second')

"""

#==============================================================================

def makeAllTests():
    suite = unittest.TestSuite()
    for klass in (TestBisect,
                  TestInsort
                  ):
        suite.addTest(unittest.makeSuite(klass))
    return suite

#------------------------------------------------------------------------------

__test__ = {'libreftest' : libreftest}

def test_main(verbose=None):
    from test import test_bisect
    suite = makeAllTests()
    test_support.run_suite(suite)
    test_support.run_doctest(test_bisect, verbose)

if __name__ == "__main__":
    test_main(verbose=True)

