
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur_head = self.head
        out_lst = []
        while cur_head:
            out_lst.append(cur_head.value)
            cur_head = cur_head.next
        out_str = str(out_lst)
        return out_str



    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        result_lst = []
        curr_node = self.head
        while curr_node:
            result_lst.append(curr_node.value)
            curr_node = curr_node.next
        return result_lst

def union(llist_1, llist_2):
    result_llist = LinkedList()
    result_set = set()

    # Linked List 1
    current_node = llist_1.head
    while current_node is not None:
        value = current_node.value
        if value not in result_set:
            result_set.add(value)
            result_llist.append(value)
        current_node = current_node.next

    # Linked List 2
    current_node = llist_2.head
    while current_node is not None:
        value = current_node.value
        if value not in result_set:
            result_set.add(value)
            result_llist.append(value)
        current_node = current_node.next

    return result_llist

def intersection(llist_1, llist_2):
    result_llist = LinkedList()
    check_set = set() # have we seen it at least once?
    result_set = set() # have we seen it at least twice?

    current_node = llist_1.head
    while current_node is not None:
        value = current_node.value
        check_set.add(value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node is not None:
        value = current_node.value
        if value in check_set and value not in result_set:
            result_set.add(value)
            result_llist.append(value)
        current_node = current_node.next

    return result_llist


if __name__ == '__main__':

    # Test 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    assert set(union(linked_list_1, linked_list_2).to_list()) == set(element_1).union(set(element_2))

    print (intersection(linked_list_1,linked_list_2))
    assert set(intersection(linked_list_1,linked_list_2).to_list()) == set(element_1).intersection(set(element_2))

    # Test 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_3 = [3,2,4,35,6,65,6,4,3,23]
    element_4 = [1,7,8,9,11,21,1]

    for i in element_3:
        linked_list_3.append(i)

    for i in element_4:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    assert set(union(linked_list_3, linked_list_4).to_list()) == set(element_3).union(set(element_4))

    print (intersection(linked_list_3,linked_list_4))
    assert set(intersection(linked_list_3, linked_list_4).to_list()) == set(element_3).intersection(set(element_4))

    # Test 3
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_5 = list(range(4, 12, 2))
    element_5.append(None)
    element_5.append(None)


    element_6 = list(range(10, 20, 2))
    element_6.append(None)

    for i in element_5:
        linked_list_5.append(i)

    for i in element_6:
        linked_list_6.append(i)


    print (union(linked_list_5,linked_list_6))
    assert set(union(linked_list_5, linked_list_6).to_list()) == set(element_5).union(set(element_6))

    print (intersection(linked_list_5,linked_list_6))
    assert set(intersection(linked_list_5, linked_list_6).to_list()) == set(element_5).intersection(set(element_6))
