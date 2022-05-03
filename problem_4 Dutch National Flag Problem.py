def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    #Since we only have 3 integers, 0, 1, 2 and sorting function is not allowed
    first_ele_index_0 = 0
    last_ele_index_2 = len(input_list) - 1
    #other_ele_index is the index we would use to traverse the list from start to end
    other_ele_index = 0
    #three modes of travsering the list:
    while other_ele_index <= last_ele_index_2:
        #1. The other_ele_index in the list gives 0
        if input_list[other_ele_index] == 0:
            input_list[other_ele_index] = input_list[first_ele_index_0]
            input_list[first_ele_index_0] = 0
            #This makes for the movement or traversing of the index along the list
            first_ele_index_0 += 1
            other_ele_index += 1
        #2. The other_ele_index in the list gives 2
        elif input_list[other_ele_index] == 2:
            input_list[other_ele_index] = input_list[last_ele_index_2]
            input_list[last_ele_index_2] = 2
            #This makes for the movement or traversing of the index along the list but thiis time around
            #the index of the last item is decreasing or in the reverse direction.
            last_ele_index_2 -= 1
        #3. The other_ele_index in the list gives 1 definitely since, 0 and 2 have aleady been taken into consideration
        #and the traverse is down in list in increasing format
        else:
            other_ele_index += 1
    return input_list
         


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 2, 0, 2, 0, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2])