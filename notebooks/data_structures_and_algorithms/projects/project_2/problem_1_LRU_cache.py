

class Node(object):

    def __init__(self, value, key=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class Queue():

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, new_node): #add new item to tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail #backlink current tail to new node
            self.tail.next = new_node #frontlink new node to current tail
            self.tail = new_node #shift tail
            self.tail.next = None #in case new node already has a `next` node.
        self.size += 1

    def dequeue(self): #pop off oldest item from head
        if self.size > 0:
            old_head = self.head
            self.head = old_head.next
            self.size -= 1
            return old_head
        else:
            return None

    def _delete(self, node): #remove node arbitrarily; needs to handle three cases for a doubly-linked list
        if self.size == 1: #if only one node, create an empty queue.
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.previous = None
        elif node == self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            left_node = node.previous
            right_node = node.next
            left_node.next = right_node
            right_node.previous = left_node
        self.size -= 1
        return

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.q = Queue()

    def put(self, hashcode, value):
        if hashcode in self.map.keys():
            old_node = self.map[hashcode]
            old_node.value = value #update mapping
            self.q._delete(old_node) #remove node from current place in queue
            self.q.enqueue(old_node) #add node onto tail of queue, now last-in.

        else:
            if self.q.size == self.capacity:
                node_to_remove = self.q.dequeue()
                hashcode_to_remove = node_to_remove.key #this is why Node class has a `key` attribute.
                del self.map[hashcode_to_remove] #remove first-in item from mapping
            new_node = Node(value=value, key=hashcode) # create new node
            self.map[hashcode] = new_node #create mapping
            self.q.enqueue(new_node) #add new node to end of queue.

    def get(self, hashcode):
        if hashcode in self.map.keys():
            node = self.map[hashcode] # retrieve node from hashmap
            self.q._delete(node) # remove node from current position in queue
            self.q.enqueue(node) #add node onto tail of queue
            return node.value
        else:
            return -1


def verbose_check(our_cache):
    print("cache map: ", {hashmap: node.value for hashmap, node in our_cache.map.items()})
    node = our_cache.q.head
    counter = 1
    print("queue: ")
    while node:
        print(f"pos: {counter} ; key: {node.key}; value: {node.value}")
        node = node.next
        counter += 1

if __name__ == '__main__':
    our_cache = LRU_Cache(5)
    our_cache.put(1, 5);
    our_cache.put(2, 10);
    our_cache.put(3, 15);
    our_cache.put(4, 20);

    # Test 1
    result1 = our_cache.get(1)
    print(result1)
    assert result1 == 5
    assert(our_cache.q.tail.value == 5) # should now be last-in item
    assert(our_cache.q.head.value == 10) # second item should now be first
    assert(our_cache.get(7) == -1) # not in the cache
    assert ({hashmap: node.value for hashmap, node in our_cache.map.items()} == {1: 5, 2: 10, 3: 15,
                                                                                 4: 20})  # assert all key-value store.
    # Test 2
    our_cache.put(5, 25) # brings us up to capacity of cache
    our_cache.put(6, 30) # brings us past capacity of cache, pushing first item off head.
    result2 = our_cache.q.head.value
    print(result2)
    assert result2 == 15 # head should now be the third item we put in
    assert(our_cache.q.tail.value == 30) #tail should be the last-in item

    # Test 3
    our_cache.put(5, "cat") # overwrite current value
    result3 = our_cache.q.tail.value
    print(result3)
    assert ((our_cache.q.tail.key == 5) & (our_cache.q.tail.value == "cat"))  # updated value should now be at tail.
    assert(our_cache.q.head.value == 15) #head should not have changed
