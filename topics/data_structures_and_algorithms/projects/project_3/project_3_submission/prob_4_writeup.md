## Dutch National Flag Problem

At first, I wrote this function to place elements in three separate lists and then concat them together using `lst.extend()`, because this *seemed* to satisfy the criterion of a single traversal. However, assuming that we are extending the list of zeros using the list of ones, and then the list of twos, we are actually traversing the lists of ones and twos twice to copy their values into the resulting array. Additionally, this creates a copy of the initial array, so would have space complexity of O(n), when there is probably a way to do it in-place for a space complexity of O(1).

I instead went for a different approach that follows the logic of partitioning the array a la quicksort.

Partition the array (of length `n`)into four sections using three cutpoints: low middle and and high.

1. `arr[0: low]` -> zeros
2. `arr[low: mid]` -> ones
3. `arr[mid: (hi - 1)]` -> unknown
4. `arr[hi : (n - 1)]` -> twos

We advance the mid marker, and make swaps based on the value at the midmarker's index. As we increase the `mid` marker's index and/or decrease the `hi` marker's index, we shrink the unknown region until the `mid` marker equals the `hi` marker, and everything is in its right place.

Time complexity is `O(n)`, because we are traversing the array and swapping out values, and the swaps operate in constant time.

Space complexity is `O(1)` because we are performing the sort in-place without creating additional objects that vary with the size of the input.
