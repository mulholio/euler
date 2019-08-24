# coding: utf-8
from largest_product import product, greatest_adjacent, ones_list, sum

def test_product():
    assert product([1]) == 1
    assert product([1, 2]) == 2
    assert product([1, 2, 7]) == 14 
    assert product([2, 9, 9, 4]) == 648

def test_sum():
    assert sum([1, 2, 3]) == 6

def test_greatest_adjacent():
    assert greatest_adjacent(12, 1) == [2]
    assert greatest_adjacent(1111589, 3) == [5, 8, 9]
    assert greatest_adjacent(11110589, 4) == [1, 1, 1, 1]
    assert greatest_adjacent(99909999, 4) == [9, 9, 9, 9]

def test_ones_list():
    assert ones_list(1) == [1]
    assert ones_list(3) == [1, 1, 1]
    assert ones_list(5) == [1, 1, 1, 1, 1]
