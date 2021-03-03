# Building a Trie

The time complexity of searching and inserting are both `O(n)` where `n` is the length of the key we're searching for or adding. We need to look at each element in the key to either see if it exists (in the case of search) or to add a new node (in the case of insert).

Space complexity would be `O(n)` where n is the number of nodes. In the worst case scenario, there would be no words that share a prefix in the trie, and thus you would have as many nodes as you had total characters in the keys. In practice however, (in making an actual autocomplete algorithm for a reasonably large dictionary of English words, for example) many keys would share prefixes, and the space complexity would be significantly reduced.
