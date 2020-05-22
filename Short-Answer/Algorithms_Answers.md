#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Arithmetic operations are O(n) time since they increase linearly with the input size n


b) Nested loops are O(n*log n). Each element must be touched at least once so O(n) for the for-loop
then the while loop adds another O(log n) because j is double in the loops body thereby reaching its "ceiling" faster.
Total O-time is found by multiplying them together.


c) This is similar to a recursive factorial problem which is O(n). This is beacuse the calculation is done one-by-one for
each value between "bunnies" and "0" (the base case).

## Exercise II
This is a binary search problem which makes this O(log n).

I'd first pick the middle floor (n/2) and drop.
    If it breaks ignore the lower floors and repeat/recurse
    If it doesn't break ignore the upper floors and repeat/recurse

