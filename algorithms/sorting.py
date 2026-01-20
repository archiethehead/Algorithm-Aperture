
def selection_sort(unsorted_list: list[int | float]) -> list[int | float]:
    """Sort a given array with the selection sort method.
 
    Args:
        unsorted_list(list of ints and or floats).
 
    Returns:
        Sorted version of unsorted_list.
 
    Raises:
        ValueError: If n is not an integer.
 
    Examples:
        >>> selection_sort([10,2,4]])
        [2,4,10]
        >>> selection_sort([12,22,3,-1,0]])
        [-1,0,3,12,22]     
    """

    for x in range(len(unsorted_list)):
        
        #We only need to check elements smaller than the current one for sorting.
        smallest = unsorted_list[x]
        smallest_index = 0

        #Index is sliced to check every element after the current one (preivous elements are sorted).
        for y in range(len(unsorted_list[x:])):
            try:
                if unsorted_list[x:][y] < smallest:
                    smallest = unsorted_list[x:][y]
                    smallest_index = y + x
            #This is the earliest point a type error can be caught wihtout interupting execution.
            except:
                raise TypeError("List must contain only integer and float variables.")

        #If a smaller value isn't found, smallest_index isn't updated, and no swap occurs.
        if smallest_index > 0:
            unsorted_list[x] += unsorted_list[smallest_index]
            unsorted_list[smallest_index] = unsorted_list[x] - unsorted_list[smallest_index]
            unsorted_list[x] = unsorted_list[x] - unsorted_list[smallest_index]

    return unsorted_list

print(selection_sort([1,5,2,3,4,6,4,23,1,2,3,5,3,2,9,0]))