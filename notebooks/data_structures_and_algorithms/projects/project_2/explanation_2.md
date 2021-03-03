## File Recursion

The base case for this recursive function is the situation in which we are looking at a path that's pointing to a file, rather than to a subdirectory, *and* that path ends with the target suffix.

If the path we are looking at is a directory, we need to call the function again on the contents of that directory, after appending the subdirectory name to the path.

(I assumed that if the path points to neither a file nor to a directory, the function should ignore it.)

The time complexity is O(n), where n is the total number of subdirectories beneath the path provided to the function. Each time we hit a subdirectory, we call the function again.

I believe the space complexity is also O(n). Memory complexity is determined by the number of return statements because each function call will be stored on the program stack.
