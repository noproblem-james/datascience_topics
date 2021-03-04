## Active Directory

This is a recursion problem with two base cases: we find the user, or we run out of child groups.

Time complexity should be linear, O(n), where n is the total number of unique child groups plus the number of users (regardless of whether they are unique or not) because we need to look through each user and child group to see if is, or contains, the user we're looking for. In other words, the function is being called recursively n times before reaching base case so its O(n), often called linear.

I believe the space complexity is also O(n), because the function is called on every subpath (child group or user) in the directory, and every function call is stored on the program stack until we hit the base case.
