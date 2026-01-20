
def nth_fibonacci(n: int) -> int:
    """Calculate the nth fibonacci number.
 
    Args:
        n (Integer): the number of times the fibonacci sequence will be carried out.
 
    Returns:
        0: When n == 0
        nth Fibonacci/Negafibonacci number.
 
    Raises:
        ValueError: If n is not an integer.
 
    Examples:
        >>> nth_fibonacci(10)
        55
        >>> nth_fibonacci(-4)
        -3     
    """

    #Fibonacci numbers can only be integers, not any other type of numeric or non-numeric value (e.g, float, string).
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    
    if n == 0:
        return 0

    #Fibonacci numbers match their negafibonacci counterparts. The same 'positive' alorithm can be used if we
    #keep track of the 'negative' status.
    negative = False
    if n < 0:
        n = abs(n)
        negative = True

    results = [0] * (n + 1)
    results[1] = 1

    for index in range(2, n + 1):
        results[index] = results[index - 1] + results[index - 2]
    
    #Check if n is odd for negafibonacci formula (alternating positive and negative)
    if negative and (n % 2 == 0): return -results[n]
    return results[n]