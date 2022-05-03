'''
Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure 
that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete
features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
Give it a try by implementing the TrieNode and Trie classes below!
'''
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        #This creates a dictionary of children
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node
'''
Finding Suffixes
Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. 
To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that 
exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for 
suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the trie, 
collecting suffixes as you go.)
'''
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        #The recursive function has to be created off the suffix function that has a single
        #argument defaulting to an empty string
        #Initializing an empty list to absorb all the suffixes as it is created.
        list_of_suffix = list()
        #defining the recursive function being created
        self.recursive_suffix(suffix, list_of_suffix)
        
        return list_of_suffix
    def recursive_suffix(self, suffix, list_of_suffix):
        for char in self.children:
            #when suffix is empty and the char(e.g. with single char like 'a')
            if self.children[char].is_word:
                list_of_suffix.append(suffix + char)
            #when the children is more than 1(e.g. with double char like 'an')
                if len(self.children[char].children) > 0:
                    suffix += char
                    self.children[char].recursive_suffix(suffix, list_of_suffix)
            #when the children is more than 1(e.g. with double char like 'an') but to ensure that an item in the 
            #list is not part of the suffix generated. e.g f should not create a suffix of 'unactory' instead of
            #'actory'
            else:
                self.children[char].recursive_suffix(suffix + char, list_of_suffix)
# Testing it all out
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
        #return
interact(f,prefix='');