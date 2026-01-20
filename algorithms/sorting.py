
def selection_sort(unsorted_list: list[int | float], ascending: bool = True) -> list[int | float]:
    """Sort a given array with the selection sort method.
 
    Args:
        unsorted_list(list of ints and or floats).
        ascending(Boolean): specifies whether or not the list is sorted in ascending order.
 
    Returns:
        Sorted version of unsorted_list.
 
    Raises:
        ValueError: If the listr contains a non numeric value, or ascending is not a boolean.
 
    Examples:
        >>> selection_sort([10,2,4], True)
        [2,4,10]
        >>> selection_sort([12,22,3,-1,0], False)
        [22,12,3,0,-1]    
    """

    if not isinstance(ascending, bool) and ascending != 0 and ascending != 1:
        raise TypeError("Ascending must be a boolean.")

    for x in range(len(unsorted_list)):
        
        #We only need to check elements smaller than the current one for sorting.
        smallest = unsorted_list[x]
        smallest_index = 0

        #Index is sliced to check every element after the current one (preivous elements are sorted).
        for y in range(len(unsorted_list[x:])):
            try:
                if ascending:
                    if unsorted_list[x:][y] < smallest:
                        smallest = unsorted_list[x:][y]
                        smallest_index = y + x
                else:
                    if unsorted_list[x:][y] > smallest:
                        smallest = unsorted_list[x:][y]
                        smallest_index = y + x
                        
            #This is the earliest point a type error can be caught wihtout interupting execution.
            except TypeError:
                raise TypeError("List must contain only integer and float variables.")

        #If a smaller value isn't found, smallest_index isn't updated, and no swap occurs.
        if smallest_index > 0:
            unsorted_list[x], unsorted_list[smallest_index] = unsorted_list[smallest_index], unsorted_list[x]

    return unsorted_list

def bubble_sort(unsorted_list: list[int | float], ascending: bool = True) -> list[int | float]:
    """Sort a given array with the bubble sort method.
 
    Args:
        unsorted_list(list of ints and or floats).
        ascending(Boolean): specifies whether or not the list is sorted in ascending order.
 
    Returns:
        Sorted version of unsorted_list.
 
    Raises:
        ValueError: If n is not an integer, or ascending is not a boolean.
 
    Examples:
        >>> bubble_sort([10,2,4], True)
        [2,4,10]
        >>> bubble_sort([12,22,3,-1,0], False)
        [22,12,3,0,-1]    
    """

    if not isinstance(ascending, bool) and ascending != 0 and ascending != 1:
        raise TypeError("Ascending must be a boolean.")

    list_length = len(unsorted_list)

    for x in range(len(unsorted_list)):
        
        has_swapped = False

        for y in range(0, list_length - x - 1):
            try:
                if ascending:
                    if unsorted_list[y] > unsorted_list[y + 1]:
                        unsorted_list[y], unsorted_list[y + 1] = unsorted_list[y + 1], unsorted_list[y]
                        has_swapped = True
                else:
                    if unsorted_list[y] < unsorted_list[y + 1]:
                        unsorted_list[y], unsorted_list[y + 1] = unsorted_list[y + 1], unsorted_list[y]
                        has_swapped = True
            except TypeError:
                raise TypeError("List must contain only integer and float variables.")

        if not has_swapped:
            break

    return unsorted_list