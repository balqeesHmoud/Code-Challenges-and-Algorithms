import pytest
import unittest

from challenge05 import *


class TestArrayIntersection(unittest.TestCase):
    def test_basic_intersection(self):
        arr1 = [1, 2, 2, 1]
        arr2 = [2, 2]
        expected = [2]
        result = array_intersection(arr1, arr2)
        self.assertCountEqual(result, expected, "The intersection should be [2]")

    def test_no_common_elements(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        expected = []
        result = array_intersection(arr1, arr2)
        self.assertCountEqual(result, expected, "The intersection should be an empty list")

    def test_all_elements_common(self):
        arr1 = [4, 9, 5]
        arr2 = [9, 4, 9, 8, 4]
        expected = [4, 9]
        result = array_intersection(arr1, arr2)
        self.assertCountEqual(result, expected, "The intersection should be [4, 9]")

    def test_duplicates_in_input(self):
        arr1 = [1, 2, 2, 1, 3]
        arr2 = [2, 2, 3, 4]
        expected = [2, 3]
        result = array_intersection(arr1, arr2)
        self.assertCountEqual(result, expected, "The intersection should be [2, 3]")

    def test_one_empty_array(self):
        arr1 = [1]
        arr2 = [1, 1, 1, 1]
        expected = [1]
        result = array_intersection(arr1, arr2)
        self.assertCountEqual(result, expected, "The intersection should be [1]")

    def test_both_empty_arrays(self):
        arr1 = []
        arr2 = []
        expected = []
        result = array_intersection(arr1, arr2)
        self.assertCountEqual(result, expected, "The intersection of two empty arrays should be an empty list")

    def test_large_numbers(self):
        arr1 = [1000000, 2000000, 3000000]
        arr2 = [3000000, 2000000, 1000000]
        expected = [1000000, 2000000, 3000000]
        result = array_intersection(arr1, arr2)
        self.assertCountEqual(result, expected, "The intersection should be [1000000, 2000000, 3000000]")

if __name__ == '__main__':
    unittest.main()

