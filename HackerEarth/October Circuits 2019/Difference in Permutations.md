Given an integer N. Consider all the possible permutations of all integers from to . Calculate the value of

 for each permutation : x=(N-p[i]) i=1-N

Determine the sum of all

for all possible permutations.

Input format

    First line: A single integer 

    denoting the number of test cases
    Second line: A single integer N.

Output format

 For each test case, print a single line containing the answer.

Constraints

SAMPLE INPUT

1
2

SAMPLE OUTPUT

2

Explanation

There are 2 possible permutations for N = 2 : p = [1, 2] and p = [2, 1].

For first permutation X = (2 - 1) + (2 - 2) = 1.

For second permutation X = (2 - 2) + (2 - 1) = 1.

So sum of X over 2 possible permutations = 2.
