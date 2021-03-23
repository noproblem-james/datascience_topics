## Min and Max of Array

Perhaps I missed something , but I think all we need to do is traverse the array, store the current min and current max, and make comparisons/updates as we go.

Time complexity is `O(n)`, because we are only traversing the array once and not doing anything fancy.
Space complexity is `O(1)` because we aren't making any copies of the array, just storing the min and max.
