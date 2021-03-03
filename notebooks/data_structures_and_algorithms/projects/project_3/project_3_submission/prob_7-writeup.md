# ## HTTP Router
`.lookup()` executes in `O(n)` time in the worst case, where `n` is the number of path-parts in the path we're looking for. This is because we still need to look through every part of the path until we get to ensure that it exists. I figure that the best case (from a time efficiency standpoint) is when the first part of the path doesn't exist in the children of the root of the trie and we return `None` (or our '404 error not found' message) after just one attempt to traverse down the trie.

`.add_handler()` has a time efficiency of of `O(n)` in the worst case scenario. We first need to iterate through the path to split it into chunks at the slash marks, and then we also need to use `insert()`, which operates in `O(n)` time for a trie.

Similar to the answer for problem 5, I believe that in the worst-case scenario, the space efficiency is `O(n)` where n is the total number of path-parts, because in the worst case, no path would be a prefix to any other path and thus each part of each path would have a separate node. This is unlikely in practice, however. The whole point of using a trie is to take advantage of a situation where many keys share the same prefix.
