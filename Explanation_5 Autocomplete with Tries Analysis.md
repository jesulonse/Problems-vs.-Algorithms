For this problem an hash map would have sufficed by storing up the known words and checking if such words exist within it. This would have 
yielded a constant time complexity of O(1) for few number, n of words and length, m of the each word.
But once, the words are many and the length becomes very long, then hash map would not meet an efficient memory use. A trie avoids the collisions of keys that sometimes occurs in hash function. Hence, a hash function would not be needed. Therefore, a Trie is 
being used. 

This problem consists of at least 4 items used to solve it:
1. Trie class which contains the root node
2. TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
3. Recursive function within the TrieNode used to recurse through the list of suffix
4. Test functions
Now that we have a function Trie, we are adding the ability to list suffixes to implement our autocomplete feature. 
To do this, we implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().
The new function is the suffixes function that we use to recurse down the trie, collecting suffixes as you go.

Time Complexity Analysis:

There are three levels for this recursive function:
a. At the point where the input argument is just the empty suffix  + the char, at this point the time complexity is O(1), constant time. Also when the char is not in the prefix of list of words
b. As the prefix increases by virtue of the no  of children increasing more than one, n>1, the suffix + the char, but under the condition that
the suffix and the char now add up to form the prefix, i.e. suffix += char. Hence, the time complexity is O(n) because it does not need to search further down since, it already has the prefix stored in the dictionary as a child. e.g. 'fu', 'fun' does not need to recurse again as it is already stored in the dictionary to generate the word 'function'
c. At the point where, the input argument does not have any alreaddy formed prefix in the dictionary, the recurse function will run with O(n) time complete the word, e.g. the word 'fun' is not a prefix for 'factory', therefore, the recurse will run in O(n) to generate the autocomplete 
of the word 'actory'.



Space Complexity Analysis:

The space complexity is O(n) by reason of the number of words in the Trie node. Note, that because the dictionary already stores some of the 
words as prefix during the recurse, it does not need to create an added space for it.



