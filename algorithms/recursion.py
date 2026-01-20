
def factorial(n: int) -> int:
    """Calculate the factorial of n with recursion.
 
    Args:
        n (Integer): The number of times the function is called recursively to calculate the factorial.
 
    Returns:
        n * (n - 1) * (n - 2) * ... *
 
    Raises:
        ValueError: If n is not an integer.
 
    Examples:
        >>> factorial(6)
        720
        >>> factorial(50)
        30414093201713378043612608166064768844377641568960512000000000000 
    """

    #Standard factorials are limited to positive, whole integers.
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    n = abs(n)

    #1 and 0 factorial are 1, and as such, can be omitted from the algorithm.
    if n == 1 or n == 0:
        return 1

    #The stack will track and multiply the result of every function call until n = 1.
    else:
        return(n * factorial(n - 1))