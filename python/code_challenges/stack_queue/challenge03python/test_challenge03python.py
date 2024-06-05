# Write your test here
import pytest
from challenge03python import delete_middle

def test_delete_middle_odd():
    assert delete_middle([1, 2, 3, 4, 5]) == [1, 2, 4, 5]

def test_delete_middle_even():
    assert delete_middle([1, 2, 3, 4]) == [1, 3, 4]

def test_delete_middle_single_element():
    assert delete_middle([1]) == []

def test_delete_middle_empty_stack():
    assert delete_middle([]) == []

def test_delete_middle_two_elements():
    assert delete_middle([1, 2]) == [2]

def test_delete_middle_large_stack():
    stack = list(range(1, 101))
    expected_stack = list(range(1, 50)) + list(range(51, 101))
    assert delete_middle(stack) == expected_stack
