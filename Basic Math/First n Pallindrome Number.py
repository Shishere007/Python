# get first n pallindrome numbers


def is_pallindrome(number):
    return str(number) == str(number)[::-1]


pall_list = []

def pallindrome_numbers(pall_count):
    sum_set = [1, 2, 10, 11, 100, 110, 1000, 1100, 10000, 11000]
    last_pall = 1
    count = len(pall_list)
    loopVar = last_pall
    set_index = 0
    add_by = sum_set[set_index]
    while True:
        if is_pallindrome(loopVar):
            pall_list.append(loopVar)
            set_index = 0
            last_pall = loopVar
            count += 1
        else:
            loopVar = last_pall
            set_index += 1
            add_by = sum_set[set_index]
        if count == pall_count:
            break
        loopVar += add_by
    return pall_list

count = 100
print (pallindrome_numbers(count))

_ = input()