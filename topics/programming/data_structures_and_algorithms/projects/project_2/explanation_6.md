## Union Intersection

Because there were no requirements about the ordering of the result linked list, it seemed like an opportunity to exploit the faster average lookup times for sets by checking to see whether each value exits in a set before we decide whether or not to append it to the resulting linked list.

For `union()`, my idea was to just define a result set, and check to see if the value of each node in the linked list already exists in the result set before appending it to the result linked list.

For `intersection()`,  my idea was to define a result set and a check set. We want to keep every value that we have seen twice--once in the first linked list and again in the second linked list. We don't want to return a value that we see twice in the first linked list. Thus, we want to basically convert the first linked list to a check set, against which we check the values in the second linked list. If a value from the second linked list is in the check set, we put it in the result set. If not, we keep going.

It's inevitable that we are going to need to look at every node in both linked lists, so we're already at O(n) where n is the total number of nodes in linked list 1 and linked list 2. For each node in each linked list, we're checking set membership and (possibly) appending to sets, with  an average time complexity of O(1) and a worst-case time complexity of O(n).
So, that makes an average-case time complexity of O(n * 1) = O(n) and a worst-case time complexity of O(n * n) = O(n^2).

The space complexity should be based on the number of unique elements in both sets. For `union()`, we're only storing each unique element once. For `intersection()`, we're storing all of the unique elements in the first linked list, and then storing them again if they appear in the second linked list.
