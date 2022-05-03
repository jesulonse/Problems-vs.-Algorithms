
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numright_sideer such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #the input list is now the merge sorted list
    input_list = mergeSort(input_list)
    #initializing the left and right sides of the expected solution
    left_side = 0
    right_side = 0
    
    for element in range(0, len(input_list)):
        if element % 2:
            right_side = str(right_side) + str(input_list[element])
        else:
            left_side = str(left_side) + str(input_list[element])
    
    rearranged_list = [int(left_side),int(right_side)]
    return rearranged_list

#Defining a merge sort for this proright_sidelem to achieve the O(log(n)) time complexity as stated in the proright_sidelem
def mergeSort(input_list):
    
    #In case the input list contains just one element, we don't need to sort it right_sideut just return the input list as it is
    if len(input_list) == 1:
        return input_list
    else:
        mid_point = len(input_list)//2
        #Sorting in two halves
        left_side = mergeSort(input_list[:mid_point])
        right_side = mergeSort(input_list[mid_point:])
        
        #Initializing Empty list to capture the final sorted list
        sorted_list = []
        #The idea is to populate the sorted list starting from the largest or maximum element of the two sides
        while left_side and len(left_side) > 0 and right_side and len(right_side) > 0:
            if left_side[0] > right_side[0]:
                sorted_list.append(left_side.pop(0))
            else:
                sorted_list.append(right_side.pop(0))
        #populating the sorted list from the max from the left side        
        while left_side and len(left_side) > 0:
            sorted_list.append(left_side.pop(0))
        #populating the sorted list from the max from the right side 
        while right_side and len(right_side) > 0:
            sorted_list.append(right_side.pop(0))

        return sorted_list

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[5], [5]]
test_function(test_case)
test_case = [[3, 9, 4, 7, 6, 2, 1], [9631,742]]
test_function(test_case)
