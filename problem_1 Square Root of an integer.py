def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
      number(int): Number to find the floored squared root
    Returns:
      int: Floored Square Root
    """
    start_i = 0
    end_i = number
    #making provision for even and odd numbers so that the value is whole value integer
    if number % 2 == 0:
      mid_i = (start_i + end_i)//2
    else:
      start_i = 1
      mid_i = (start_i + end_i)//2
      
    
    while mid_i < end_i:
        #using binary search, we are working towards ensuring that the mid value and end value meet at the center or
        #iterate towards the same point and value
        end_i = mid_i
        mid_i = (end_i + number//end_i)//2 
    return mid_i    
    
       
# print(sqrt(28))
print ("Pass" if  (3 == sqrt(9)) else "Fail") # expected result: Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") # expected result: Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # expected result: Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") # expected result: Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # expected result: Pass
