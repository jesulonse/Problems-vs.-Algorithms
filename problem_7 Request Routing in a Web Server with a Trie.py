# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        ## Initialize this node in the Trie
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, web_add, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for web_path in web_add:
            #we are recursively adding nodes
            current_node.insert(web_path)
            current_node = current_node.children[web_path]

        current_node.handler = handler

    def find(self, web_add):
        # Starting at the root, navigate the Trie to find a match for this path
        current_node = self.root
        # Return the handler for a match, or None for no match
        for web_path in web_add:
            if web_path not in current_node.children:
                return None
            current_node = current_node.children[web_path]
        
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None #Instead of False

    def insert(self, web_add):
        # Insert the node as before
        self.children[web_add] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, handler_for_404):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(handler)
        self.handler_for_404 = handler_for_404


    def add_handler(self,web_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        web_add = self.split_path(web_path)
        self.router.insert(web_add, handler)

    def lookup(self, web_path):
        # lookup path (by parts) and return the associated handler
        web_add = self.split_path(web_path)
        finder = self.router.find(web_add)
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        if len(web_add) == 0:
            return self.router.handler#instead of using None, I used self.route.handler making sure that an empty address 
            #means it is the root path.e.g we bave an address: "/" or " "
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if finder == None:
            return self.handler_for_404
        else:
            return finder

    def split_path(self, web_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        part_split = web_path.split('/')
        return [i for i in part_split if i != '']

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

print("********Another Sample*************")
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/menu/goods", "menu handler")  # add a route
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/menu")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/menu/goods")) # should print 'menu handler'
print(router.lookup("/menu/goods/")) # should print 'menu handler' or None if you did not handle trailing slashes
print(router.lookup("/menu/goods/services")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/menu/goods/services/bags")) # should print 'not found handler' or None if you did not implement one

print("********Another Sample*************")
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/menu/goods/shirts", "menu/goods handler")  # add a route
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/menu")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/menu/goods")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/menu/goods/")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/menu/goods/shirts/")) # should print 'menu/goods handler' 
print(router.lookup("/menu/goods/services/bags")) # should print 'not found handler' or None if you did not implement one
