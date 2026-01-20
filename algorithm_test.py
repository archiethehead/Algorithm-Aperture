import pytest
import timeit
from algorithms import dynamic_programming

class Test_fibonacci:
    @pytest.mark.parametrize("n, expected", [
        (0, 0), 
        (1, 1), 
        (10, 55), 
        (-3, 2), 
        (-4, -3)
    ])
    def test_(self, n, expected):
        assert dynamic_programming.nth_fibonacci(n) == expected