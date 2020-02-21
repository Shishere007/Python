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

position = int(input("Position : "))
print (nth_pallindrome(position))

_ = input()