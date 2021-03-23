class RouteTrieNode:

    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}
    def __repr__(self):
        return f"{self.__class__.__name__}(handler={self.handler}, children= {self.children})"


class RouteTrie:

    def __init__(self, root_handler=None):
        self.root = RouteTrieNode(handler=root_handler)

    def insert(self, path_parts, handler):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, path_parts):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                return None
            else:
                current_node = current_node.children[part]
        handler = current_node.handler
        return handler


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.rt = RouteTrie(root_handler=root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.rt.insert(path_parts, handler)

    def lookup(self, path):
        if path == "/":
            return self.rt.root.handler
        path_parts = self.split_path(path)
        handler = self.rt.find(path_parts)
        if handler is None:
            return self.not_found_handler
        else:
            return handler
    def split_path(self, path):
        return path.strip("/").split("/")


if __name__ == "__main__":
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")  # add a route
    # some lookups with the expected output
    print(router.lookup("")) # should print 'not found handler'
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler'
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler'
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
