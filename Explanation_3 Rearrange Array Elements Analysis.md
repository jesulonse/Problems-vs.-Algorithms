Rearrange Array Elements makes use of merge sort algorithm in order to achieve the time complexity of O(nlog(n)).
The Merge sort algorithm uses binear search algorithm to divide and conquer the problem.
Afterwhich the sorted list is populated with the merged sorted list from maximum to minimum.
Therefore, the Rearrange Array elements function is used to break the list into two numbers whose sum is maximum.

Time Complexity Analysis:

Since the Merge Sort algorithm is used to solve this problem, the time complexity is linearithmic.i.e. O(nlog(n)). 
There are 3 while loops passing through the input list to generate the merge sort list.
Each while loop is O(log(n)). Since it is traversing the list 3 times, we have 3 * log(n). Hence, n * log(n).
Hence, the O(nlog(n)) time complexity for the merge sort
Although the Rearrange Array elements function receives the merge sorted list as input, the single for loop in it makes
the time complexity for the function to be O(n), i.e. Linear Time complexity. Which means the more the input from the 
merge sorted input list, the more time it takes to loop through it
Therefore, the time complexity for this problem is the worst-case scenerio which is O(nlog(n)).

Space Complexity Analysis:

The space occupied using the merge sort algorithm is O(n). This means the algorithm takes a lot of memory space based on the 
input size. The memory space it takes is O(n) as we divide the input list and store it into memory where the total space used in making all the list and merging back into one list(but a sorted list this time around) is the total elements, n, in it.
Therefore, the time Complexity is linear, O(n).
