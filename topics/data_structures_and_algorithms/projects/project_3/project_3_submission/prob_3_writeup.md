## Rearrange Array Digits

Once we have a sorted array, we can simply iterate over it, convert every digit to a string, append the even-indexed elements to one string and the odd-indexed elements to another string, and, once we've exhaused the elements in the array, convert the two resultant strings to integers.

Because the most efficient sorting algorithms like mergesort and heapsort all operate with a time efficiency of `O(n*log(n))`, we don't introduce substantially more time complexity by iterating through the (sorted) array a second time. The complexity of two "adjacent" loops is O(n) + O(n) --> O(n + n) --> O(2n). Because constants drop out of complexity calculations, `O(2n)` reduces to `O(n)`.

Converting the data type from `int` to `str` and back operates in constant time.

The space complexity is `O(n)`, because we need to create two separate arrays (strings) from the input before returning them.
