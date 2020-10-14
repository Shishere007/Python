def is_pallindrome(number):
    return str(number) == str(number)[::-1]


def nth_pallindrome(position):
    digit_list = list(str(position))
    length = len(digit_list)
    digit_list.pop(0)
    digit_list = digit_list + digit_list[::-1]
    number = int("".join(digit_list))
    if position == pall_position(number) and is_pallindrome(number):
        return number
    digit_list_copy = list(str(position))
    digit_list_copy[0] = str(int(digit_list_copy[0]) - 1)
    temp = digit_list_copy[::-1]
    temp.pop(0)
    digit_list_copy += temp
    number = int("".join(digit_list_copy))
    if position == pall_position(number) and is_pallindrome(number):
        return number


def nearest_pall(number):
    while True:
        if is_pallindrome(number):
            return number
        number += 1


def pall_position(number):
    digit_list = list(str(number))
    length = len(digit_list)
    if length % 2 == 0:
        digit_list = ["1"] + digit_list[: int(length / 2)]
        position = int("".join(digit_list))
    else:
        digit_list = digit_list[: int(length / 2) + 1]
        digit_list[0] = str(int(digit_list[0]) + 1)
        position = int("".join(digit_list))
    return position


test_case = int(input())

for _ in range(test_case):
    x, k = map(int, input().split())
    near_pall = nearest_pall(x)
    position = pall_position(near_pall)
    new_pall_pos = position + k - 1
    print(nth_pallindrome(new_pall_pos))


"""
A palindromic number is a number that remains the same when its digits are reversed. Your task is to get the palindrome number greater than or equal to

.

Input format

    First line: Integer 

 denoting the number of test cases
Each of the following
lines:

     First line: Two space-separated integers 

and

Output format

Print
lines, each line contains the answer for the

case.

Constraints

SAMPLE INPUT

4
10 23
1 12
5 26
12 11

SAMPLE OUTPUT

232
33
212
121


"""

