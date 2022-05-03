The project is designed such that we do not use any internal maths function of sqrt.
Hence, the function(Sqrt()) was created to solve the square root of integer.
It was also mandated that the time complexity should be O(log(n)). Hence, to make it logarithmic, we use the 
Binary Search principle which divides the input in half at each iteration.

Time Complexity Analysis:

The binary Search algorithm of dividing the input in half for each iteration was used as required. This ensures that the runtime is 
logarithmic. i.e. the iteration starts with i = n, n/2, n/2**2, n/2**3, ....., n/2**k
Therefore, n/2**k = 1
           n = 2**k
        taking log of both sides to base 2:
        log2 n = log2 2**k
        log2 n = klog2 2
        k = log2 n. Therefore, we have O(log2 n).i.e. O(log(n))

Space Complexity Analysis:

Because we are iterating through the Binary Search Algorithm, we need two variables(i.e mid element and end element in this case), at each point of iteration, to search through the elements. And we do not need any other variable, the space complexity remains constant despite the number of elements. Therefore, the space complexity is O(1).



           