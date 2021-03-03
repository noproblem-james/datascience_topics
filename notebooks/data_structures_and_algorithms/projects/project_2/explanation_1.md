## LRU Cache
I conceived of an LRU cache as a combination of a Queue and a Map.
A map allows a fast (constant time) lookup operation, and a queue allows us to keep an order without an index.
A queue built from a doubly linked list can perform insertions and deletions in constant time.  

I decided to use the built-in Python `dict` type as a map, and then build a queue as a separate class. I then wrote an LRU class that has its own map and its own (DLL) queue working in concert.  
Incorporating the traits of queue directly into the LRU cache class would have been shorter, but I found it more explicit and easier to conceptualize when those functions exist separately.  

I assumed that actually writing a hash function was outside the scope of this problem.

I'm fairly confident that the `.put()` method operates in constant time, as there are no loops in the code. We are just looking up entries in a dict and overwriting the values if necessary. Any time we "use" an element in the cache, either by or putting it in the cache or getting it out, we need to reorder the elements such that the most recently used element moves to the tail. This necessitates deleting a node and enqueueing it. Because a linked-list data structure does not have an index, there is no need to reindex it when adding or removing elements. This means there is no need to iterate over the entire queue, and the runtime is independent of the size of the queue.

Time efficiency for `put()` and `.get()` should be O(1), i.e., constant time. Space complexity should be O(n), i.e. linear, where n is the size of the cache.

#### Note:
According to the [python wiki](https://wiki.python.org/moin/TimeComplexity) the "Amoritized Worst Case" time efficiency of the `.put()` and `.get()` operations for python dicts is O(n) because of the unlikely possibility of hash collisions. So, although the instructions say "All operations must take O(1) time," I assume that means in the *average case*. AFAIK, there is no data structure that can do lookups in constant time in the worst case. The worst case here is sufficiently unlikely that we could probably discount it.
