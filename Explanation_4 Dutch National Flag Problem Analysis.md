The problem has just 3 element types: 0, 1, 2. Hence, to sort it, the first element should be 0, while the last
elemet will be 2. While the middle element would be definitely 1.
therefore, the indexes with regards to the first, last and other element is created to enable us traverse the list.


Time Complexity Analysis:

Based on the fact that there are three types of member in the list, we have 3n, Therefore, the function will traverse the list starting from 0 through to 2. If the number of element type was increased to m, it would then be m * n where m is constant. Therefore, the time complexity would be linear, O(n). That means, the more the number of elements type and memebers of the list, the more the runtime required to traverse the list and sort it.


Space Complexity Analysis:

The space occupied in memeory is constant as there are three types of no. i.e. 0,1,2 that is being traversed as we solve this problem. No matter, the number of elements, the traverse, is with reepect to the first,0 , the middle,1 and last,2. Hence, the time complexity is not changing with respect to the number of elements(n) in the list. Therefore, the space complexity is constant, O(1).
