
import sorting

def search(data: list[int | float]) -> dict[str, int | float]:
    """Search an array for various statistical values.
 
    Args:
        data(list of ints and or floats)
 
    Returns:
        dict[
        smallest:,
        largest:,
        median:,
        Q1:,
        Q3:,
        Mode
        ]
 
    Raises:
        ValueError: If the list contains a non numeric value.
 
    Examples:
        >>> search([1,1,2,3,4,5,6,7,8,9])
        {'smallest': 1,
        'largest': 9,
        'median': 4.5,
        'Q1': 2,
        'Q3': 7,
        'Mode': [1]}
    """
    
    #Since we know ascending is a Boolean, the only error that can occur is a TypeError, meaning we can
    #catch an invalid entry here, utilising the sort function.
    try:
        sorted_data = sorting.selection_sort(data, ascending = True)

    except TypeError:
        raise TypeError("List must contain only integer and float variables.")

    data_length = len(sorted_data)
    if data_length % 2 == 0:
        odd = False
    else:
        odd = True

    smallest_value = sorted_data[0]
    largest_value = sorted_data[-1]

    #Median positioning changes based on the even/odd state of an array.
    if odd:
        median_value = sorted_data[(data_length // 2)]
        first_half = sorted_data[0:(data_length // 2)]
        second_half = sorted_data[(data_length // 2) + 1:]
    else:
        median_value = (sorted_data[((data_length // 2)) - 1] + sorted_data[(data_length // 2)]) / 2
        first_half = sorted_data[0:(data_length // 2)]
        second_half = sorted_data[(data_length // 2):]
    
    if odd:
        Q1 = (first_half[(len(first_half) // 2) - 1] + first_half[(len(first_half) // 2)]) / 2
        Q3 = (second_half[(len(second_half) // 2) - 1] + second_half[(len(second_half) // 2)]) / 2
    else:
        Q1 = first_half[(len(first_half) // 2)]
        Q3 = second_half[(len(second_half) // 2)]
    
    mode = {}
    for num in sorted_data:
        if not num in mode:
            mode[num] = 1
        else:
            mode[num] += 1
    
    mode_value = [x for x, y in mode.items() if y == max(mode.values())]


    return {
        "smallest": smallest_value,
        "largest": largest_value,
        "median": median_value,
        "Q1": Q1,
        "Q3": Q3,
        "Mode": mode_value
    }

print(search([1,1,2,3,4,5,6,7,8,9]))