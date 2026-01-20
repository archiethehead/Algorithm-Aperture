
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

class palindrome_counter():

    def __init__(self):
        self.memoization_table = {}
    
    def check_palindrome(self, string, x, y):
        """Recursively check if the given string is a palindrome
    
        Args:
            string (String): the given string begin evaluated as a plaindrome
            x (Integer): the current index we're looking at
            y (Integer): the current sub-index we're looking at
    
        Returns:
            True: when the given string is palindrome
            False: if othewise
    
        Raises:
            N/A
    
        Examples:
            >>> check_palindrome("abba", 0, 0)
            True  
        """
        
        if x >= y:
            return True
        
        current_state = (x, y)
        if current_state in self.memoization_table:
            return self.memoization_table[current_state]
        
        is_palindrome = (string[x] == string[y] and self.check_palindrome(string, x + 1, y - 1))

        self.memoization_table[current_state] = is_palindrome

        return is_palindrome

    def check_substring(self, string: str) -> int:
        """Counts the number of substring palindromes in a given string
        
            Args:
                string (String): the given string begin evaluated for it's substrings
        
            Returns:
                substring_count(Integer)
        
            Raises:
                N/A
        
            Examples:
                >>> check_palindrome("abba")
                6
            """
        


        self.memoization_table = {}
        index = 0
        substring_count = 0

        for x in range(len(string)):
            for y in range(x, len(string)):
                if self.check_palindrome(string, x, y):
                    substring_count += 1
        return substring_count
    
#GeeksforGeeks (2016). Palindrome Substrings Count. [online] GeeksforGeeks. 
#Available at: https://www.geeksforgeeks.org/dsa/count-palindrome-sub-strings-string/.