## Huffman coding

This was a tough one. I got stuck a few times, and I had to consult the interwebs. Some of my logic comes from Bhrigu Srivastava [here](http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/).

I at first thought I could use a combination of a standard queue and a binary tree to create the Huffman tree. The visualization examples provided do not make clear that once two nodes are merged, the new node needs to be inserted into the queue at a specific place, according to the combined frequency of the new node. Because queues do not have a notion of order, I had to research and utilize another data structure that we haven't learned about: a priority queue, where each node has both a value and a priority assigned. I assumed that actually implementing a priority queue or binary heap was outside the scope of this problem.

Creating the frequency count using Counter should only take linear time O(n), because it needs to iterate over the input (string) and check to see if that character is already in the dictionary (constant time, O(1), on average).

If we didn't use a priority queue, we would need to look at (potentially) every node in the queue to insert a new node in-order. The priority queue is implemented using Binary Heap, which supports `insert()` and `extractmax()`operations in O(logn) time. Because we must insert (`put()`) and/or extractmax (`get()`) for each unique character in the string, we are performing an O(logn) operation n times, where n is the number of unique characters. The building of the Huffman tree is the chokepoint in terms of time complexity.

Finally, I added some logic to get the actual size of the Huffman code after it is converted to a byte array. Without that step, there is actually no compression happening by translating the original string to a longer string of ones and zeros. I'm still not totally sure if I'm comparing apples to apples.

I believe the space complexity to be O(n), i.e, it is a linear function of the number of unique characters in the input.  We need to count and store every character in the input, and the Huffman tree has a maximum depth based on the number of unique letters in the input.
