
def rotated_array_search(input_list, target):
    if target not in input_list:
        return -1
    #defining the indexes
    start_index = 0
    end_index = len(input_list) - 1
    mid_index = (start_index + end_index)//2
    target_index = input_list.index(target)
    input_list = input_list[start_index:end_index]
   
    if target == input_list[mid_index]:
        return mid_index
    #target index is less than mid_index
    elif target_index <  mid_index:
        end_index = mid_index - 1
        return rotated_array_search(input_list, target)   
    #target index is more than mid_index  
    elif target_index > mid_index:
        start_index = mid_index + 1
        if start_index == target_index:
            return start_index
        if start_index < target_index:   
            end_index = len(input_list) - 1
            return rotated_array_search(input_list, target)
       
    return -1    
#Lineaer Search function  
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

#test function
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
