from itertools import permutations
from math import factorial
testCase = int(input())
while testCase > 0 :
    testCase -= 1
    number = int(input())
    digitList = [loopVar for loopVar in range(1,number + 1)]
    tempSum = 0
    for loopVar in digitList :
        tempSum += (number - loopVar)
    totalSum = factorial(number) * tempSum
    print (totalSum) 


# Completed