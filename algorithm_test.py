import pytest
import timeit
from algorithms import dynamic_programming
from algorithms import sorting

class Test_fibonacci:
    @pytest.mark.parametrize("n, expected", [
        (0, 0), 
        (1, 1), 
        (10, 55), 
        (-3, 2), 
        (-4, -3)
    ])
    def test_nth_fibonacci(self, n, expected):
        assert dynamic_programming.nth_fibonacci(n) == expected

@pytest.mark.parametrize("data, ascending, expected", [
        ([1, 2, 5, 6, 3, 2, -1], True, [-1, 1, 2, 2, 3, 5, 6]), 
        ([1, 2, 5, 6, 3, 2, -1], False, [6, 5, 3, 2, 2, 1, -1])
    ])
class Test_sort:
    def test_selection_sort(self, data, ascending, expected):
        assert sorting.selection_sort(data.copy(), ascending) == expected

    def test_bubble_sort(self, data, ascending, expected):
        assert sorting.bubble_sort(data.copy(), ascending) == expected