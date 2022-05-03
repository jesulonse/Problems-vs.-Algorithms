def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_value = 0
    max_value = 0
    for i in ints:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    return min_value, max_value

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
num_list = [i for i in range(0, 100)]  # a list containing 0 - 99
sorted_list = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)
random.shuffle(num_list)
random.shuffle(sorted_list)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 99) == get_min_max(num_list)) else "Fail")
print ("Pass" if ((0, 999) == get_min_max(sorted_list)) else "Fail")
