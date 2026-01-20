import pytest
import random
from algorithms import dynamic_programming
from algorithms import sorting
from algorithms import recursion
from algorithms import randomised
from algorithms import search
from algorithms import brute_force

# Dynamic Programming

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
    
class Test_palindrome:

    counter = dynamic_programming.palindrome_counter()

    @pytest.mark.parametrize("string, expected", [
        ("abba", 6), 
        ("())(", 6), 
    ])

    def test_palindrome(self, string, expected):
        assert self.counter.check_substring(string) == expected

fib_data = 1000

def test_nth_fibonacci_performance(benchmark):
    benchmark(dynamic_programming.nth_fibonacci, fib_data)

palindrome = "())("
def test_palindrome(benchmark):
    counter = dynamic_programming.palindrome_counter()
    benchmark(counter.check_substring, palindrome)

# Sorting Algorithms

@pytest.mark.parametrize("data, ascending, expected", [
        ([1, 2, 5, 6, 3, 2, -1], True, [-1, 1, 2, 2, 3, 5, 6]), 
        ([1, 2, 5, 6, 3, 2, -1], False, [6, 5, 3, 2, 2, 1, -1])
    ])

class Test_sort:

    def test_selection_sort(self, data, ascending, expected):
        assert sorting.selection_sort(data.copy(), ascending) == expected

    def test_bubble_sort(self, data, ascending, expected):
        assert sorting.bubble_sort(data.copy(), ascending) == expected
    
    def test_merge_sort(self, data, ascending, expected):
        assert brute_force.merge_sort(data.copy(), ascending) == expected

sort_data = [random.randint(0, 1000) for x in range(1000)]

def test_selection_sort_performance(benchmark):
    benchmark(sorting.selection_sort, sort_data.copy(), True)

def test_bubble_sort_performance(benchmark):
    benchmark(sorting.bubble_sort, sort_data.copy(), True)

def test_merge_sort_performance(benchmark):
    benchmark(brute_force.merge_sort, sort_data.copy(), True)



# Randomisation

def test_randomisation():
    deck_1 = randomised.shuffle_deck()
    deck_2 =  randomised.shuffle_deck()

    assert deck_1 != deck_2, "The shuffle produced identical results twice."

def test_randomisation_performance(benchmark):
    benchmark(randomised.shuffle_deck)

# Recursion

class Test_factorial:
    @pytest.mark.parametrize("n, expected", [
        (6, 720), 
        (50, 30414093201713378043612608166064768844377641568960512000000000000), 
        (-3, 6), 
    ])
    def test_nth_fibonacci(self, n, expected):
        assert recursion.factorial(n) == expected

factorial_data = 50

def test_factorial_performance(benchmark):
    benchmark(recursion.factorial, factorial_data)

# Search

class Test_search:
    @pytest.mark.parametrize("data, expected", [
        ([1,1,2,3,4,5,6,7,8,9], {'smallest': 1, 'largest': 9, 'median': 4.5, 'Q1': 2, 'Q3': 7, 'Mode': [1]})
    ])
    def test_search_func(self, data, expected):
        assert search.search(data) == expected

search_data = [1,1,2,3,4,5,6,7,8,9]

def test_search_performance(benchmark):
    benchmark(search.search, search_data)