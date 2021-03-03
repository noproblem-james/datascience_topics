## Problem 1: Square Root of an Integer

Time complexity is `O(log(n))`. Space complexity is `O(1)`.
I used the "Babylonian method" for approximating square roots (one of the oldest known algorithms). We start with an initial guess, and then update that guess until the answers converge to a desired level of precision. Because we are returning only the integer answer, the algorithm has converged when the guess and the updated guess are identical.

Per [Wikipedia](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots):
>The basic idea is that if `x` is an overestimate to the square root of a non-negative real number `S` then
`S / x` will be an underestimate, or vice versa, and so the average of these two numbers may reasonably be expected to provide a better approximation.

**Pseudocode**
```
1. Make an initial guess -- here we use the input (`n`), add 1, and (floor) divide by 2
2. Update that guess by:
  a. (floor) dividing the input by the previous guess
  b. then adding the result to the previous guess
  c. then (floor) dividing the result by 2
3. when initial guess and updated guess are the same, return the guess
```

As mentioned above, we need to start with an initial (seed) value that is greater than the actual square root--but ideally not by much. We could have devised the seed value in a number of clever ways, but here I went for something simple. We know that only in two cases is the actual square root of an integer larger than that integer divided by two -- the square root of two and the square root of three. In both cases, we can add one to ensure that our initial guess is larger than the square root, and this addition will be proportionally smaller as our input grows, which doesn't add significantly to the amount of time required for convergence.

This last part of updating the guess is crucial. We are essentially (but not exactly) halving our guess each time, which produces a `O(log(n))` time complexity.

I tested this myself by building the following results table using the first thirty perfect squares. We can see that although the input is increasing exponentially, the number of iterations is increasing less-than linearly and is close to log-base-2 of the input.

| input | output | iterations | log2(input) |
|-------|--------|------------|-------------|
| 1     | 1      | 0          | 0.0         |
| 4     | 2      | 1          | 2.0         |
| 9     | 3      | 2          | 3.0         |
| 16    | 4      | 3          | 4.0         |
| 25    | 5      | 3          | 4.0         |
| 36    | 6      | 3          | 5.0         |
| 49    | 7      | 4          | 5.0         |
| 64    | 8      | 4          | 6.0         |
| 81    | 9      | 4          | 6.0         |
| 100   | 10     | 4          | 6.0         |
| 121   | 11     | 5          | 6.0         |
| 144   | 12     | 5          | 7.0         |
| 169   | 13     | 5          | 7.0         |
| 196   | 14     | 5          | 7.0         |
| 225   | 15     | 5          | 7.0         |
| 256   | 16     | 5          | 8.0         |
| 289   | 17     | 5          | 8.0         |
| 324   | 18     | 5          | 8.0         |
| 361   | 19     | 6          | 8.0         |
| 400   | 20     | 6          | 8.0         |
| 441   | 21     | 6          | 8.0         |
| 484   | 22     | 6          | 8.0         |
| 529   | 23     | 6          | 9.0         |
| 576   | 24     | 6          | 9.0         |
| 625   | 25     | 6          | 9.0         |
| 676   | 26     | 6          | 9.0         |
| 729   | 27     | 6          | 9.0         |
| 784   | 28     | 6          | 9.0         |
| 841   | 29     | 6          | 9.0         |
| 900   | 30     | 6          | 9.0         |
