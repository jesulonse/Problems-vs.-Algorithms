The Search in a Rotated Sorted Array has a binary Search and Recurive Function operating within it.
The Binary Search is to check for the shortest path to get to the target which is the mid-element. 
While the Recursive function is iterate through the list to ensure that the mid-element is obtained 
whether it is actually at the middle of the list or at either half of the list.
The beauty of this problem is that the Binary Search algorithm ensures that the Recursive function does not 
need to traverse through the whole list but in a binary Search way, thereby reducing runtime and memory space 
used.

Time Complexity Analysis:

The time Complexity of a Binary Search is logarithmic O(log(n)) due to it applying divide and rule principle.
The time complexity of the Recursive function is linear O(n). This is the due to the more input, n of the list
, the more the runtime required to traverse the list.
But because of the Binary search algorithm applied to this problem, the program is more efficient with the recursive-binary search.
If the target is exactly the middle of the list:
Time complexity, T(n) = O(1) since the target is directly at the middle of the list which is the best case scenerio
The worse-case scenerio would for the target being at either extremes of the list or the value is not in the list. In this case,
the time complexity is T(n) = O(log(n)) for the binary search.
But since we apply a Recursive function to achieve our aim, the time complexity for this problem is O(n).

Space Complexity Analysis:

At the instance of the target being the middle element, the space complexity is exactly O(1) since it is independent of the input
elements of the list.
Once the target is at the extreme or not in the list, the binary search would traverse through the list in logarithmic manner, hence,
the memory space for it would be O(log(n)).


