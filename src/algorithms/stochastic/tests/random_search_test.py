#!/usr/bin/env python

import unittest

import os

os.sys.path.append("..")

from random_search import objective_function, random_vector, search


class TestRandomSearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2]

    def test_objective_function(self):
        self.assertEqual(objective_function(self.data), 5)

    def test_random_vector(self):
        minmax = [[1, 2], [2, 3]]

        self.assertEqual(minmax[0][0], 1)

        rv = random_vector(minmax)

        self.assertEqual(len(rv), 2)
        self.assertTrue(minmax[0][0] <= rv[0] <= minmax[0][1])
        self.assertTrue(minmax[1][0] <= rv[1] <= minmax[1][1])

    def test_search(self):
        problem_size = 2
        search_space = [[-5, 5]] * problem_size
        #
        max_iter = 100
        #
        best = search(search_space, max_iter)
        #
        self.assertIsNotNone(best)
        self.assertTrue(-5 <= best['cost'] <= 5)


if __name__ == '__main__':
    unittest.main()
