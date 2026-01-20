
def merge_sort(unsorted_list: list[int | float], ascending: bool = True) -> list[int | float]:
    """Break down an array recursively into smaller, more manageable, sortable arrays
 
    Args:
        unsroted_list(list of ints and or floats)
        ascending(bool): specifies whether or not the list is sorted in ascending order.
 
    Returns:
        left(list[int | float])
        rigt(list[int | float])
        ascending(bool)
 
    Raises:
        N/A
 
    Examples:
        >>> merge_sort([1,2,3,4,53,2,2,3,4], True)
        [1]
        [2]
        [3]
        [4]
        [1, 2]
        [3, 4]
        [53]
        [2]
        [3]
        [4]
        [2]
        [3, 4]
        [2, 53]
        [2, 3, 4]
        [1, 2, 3, 4]
        [2, 2, 3, 4, 53] 
    """

    #A list that is empty, or contains one element, it sorted by definition.
    if len(unsorted_list) <= 1: return unsorted_list


    left = unsorted_list[:(len(unsorted_list) // 2)]
    right = unsorted_list[(len(unsorted_list) // 2):]

    left_merge_sort = merge_sort(left, ascending)
    right_merge_sort = merge_sort(right, ascending)

    print(left_merge_sort)
    print(right_merge_sort)

    return merge(left_merge_sort, right_merge_sort, ascending)


def merge(left: list[int | float], right: list[int | float], ascending: bool = True) -> list[int | float]:
    """Merge broken down arrays together, but in order of size.
 
    Args:
        left(list of ints and or floats)
        right(list of ints and or floats)#
        ascending(bool)
 
    Returns:
        sorted_list(list[int | float])
 
    Raises:
        ValueError: If the list contains a non numeric value.
 
    Examples:
        >>> merge([1],[2], True)
        [1, 2]
    """
    
    sorted_list = []
    x = 0
    y = 0

    while x < len(left) and y < len(right):

        try:
            
            if ascending:
                is_bigger = left[x] < right[y]
            

            else:
                is_bigger = left[x] > right[y]

        except TypeError:
            raise TypeError("Ascending must be a boolean.")

        if is_bigger:
            sorted_list.append(left[x])
            x += 1
        
        else:
            sorted_list.append(right[y])
            y += 1

    sorted_list.extend(left[x:])
    sorted_list.extend(right[y:])
    return sorted_list

print(merge_sort([1,2,3,4,53,2,2,3,4]))