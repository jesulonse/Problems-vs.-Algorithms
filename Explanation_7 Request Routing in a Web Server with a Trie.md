For this problem an hash map would have sufficed by storing up the known words and checking if such words exist within it. This would have 
yielded a constant time complexity of O(1) for few number, n of words and length, m of the each word.
But once, the words are many and the length becomes very long, then hash map would not meet up with an efficient memory use. A trie avoids the collisions of keys that sometimes occurs in hash function. Hence, a hash function would not be needed. 
Also regular expressions would have been sufficient for this problem but for slow performance especially with certain strings. Therefore, a Trie is being used.

We implemented a Trie to solve this problem. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node "/"
For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler.i.e. whether we have a handler or not or whether the path is the root handler
We split things based on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:
(root, None) -> ("about", None) -> ("me", "About Me handler")
We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.



Time Complexity Analysis:

We have a web address or url. First, we split it by the slash '/'. Then, we recursively add the broken down path from the split to the handler.
The more the paths(n) in the web address, the more we need to recurse to insert it into the handler. Hence, the  time complexity of O(n).
It is a linear time complexity, that the more the paths(n), the more the time(T(n)) it would take to recurse it into the handler.


Space Complexity Analysis:

The larger the web address, the more the space in memeory that would be required to store it in the handler as the paths in the web address is first split into paths with size(n). Hence, if we have a web address that has 50 paths, n = 50 and another web address has 5 paths, n = 5.
The web address with 50 paths would occupy more memory space to place it in the handler than that of 5. Hence, the space complexity is O(n)


