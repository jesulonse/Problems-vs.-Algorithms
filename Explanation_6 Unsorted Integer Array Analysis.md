To solve this problem, we first initiate the minimum and maximum values.
As we iterate or traverse through the list, the minimum value and maximum values is saved in the tuple.
Once, a number that is less than that in the tuple is encountered, the minimum value is replaced with such value.
Likewise, once a maximum value is encountered during the traverse through the list, the initial maximum value is replaced 
with the current maximum value until the whole list is traversed

Time Complexity Analysis:

Because the minimum and maximum values are being populated in the tuple as the list is being traversed in a list, it takes a runtime of O(n).
The more, the values of the list, the more the time, T(n), it takes to traverse the list.
Therefore, the time complexity is O(n)


Space Complexity Analysis:

The memory space taken up during the traverse is for two elements (i.e. the maximum and minimum) at any point of the traverse through the 
list of items. This memory space does not increase with respect to the number of elements in the list. Hence, the memory occupied per runtime is constant. Therefore, the space complexity is constant, O(1)




