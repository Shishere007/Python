def is_pallindrome(number):
    return str(number) == str(number)[::-1]


print (is_pallindrome(input("String or Number : ")))

_ = input()