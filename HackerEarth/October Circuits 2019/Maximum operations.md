The Fibonacci sequence is defined as F[n] = F[n-1] + f[n-2]
You have developed two sequences of numbers. The first sequence that uses the XOR operation instead of the addition method is called the Xoronacci number.
It is described as follows:

X(n) = X(n-1) XOR X(n-2)

The second sequence that uses the XNOR operation instead of the addition method is called the XNoronacci number. It is described as follows:

E(n) = E(n-1) XNOR E(n-2)

The first and second numbers of the sequence are as follows:

X(1) = E(1) = a
X(2) = E(2) = b

You have also defined the following constraint:

'The minimum number of bits that that is used while representing the  term must be greater than equal to 3. It must be equal to the minimum number of bits that is required while respresenting the maximum pair (first number, second number) of the respective sequences.'

Your task is to determine the value of max(X(n),E(n))

Input format

    ☼ First line: t denoting the number of test cases
    ☼ next t lines :three integers a,b and n

denoting the number of test cases
Next
lines: Three integers , , and

Output format

Print a single integer for each test case.


SAMPLE INPUT

3
3 4 2
4 5 3
325 265 1231232

SAMPLE OUTPUT

4
6
265


 Explanation

For First Test Case

 

Ist sequence  elements are                  3       4       7

IInd sequence elements are                 3       4       0

 

hence max(E(2),X(2))=4
