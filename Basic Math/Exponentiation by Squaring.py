def exp( number, power):
    if ( power == 1 ):
        return number  
    if ( power % 2 == 0 ):
        return exp( number * number, power // 2 )
    return number * exp( number * number, power // 2 )
number = int(input("Number : "))
power = int(input("power : "))
print (f"Answer : {exp(number,power)}")

_ = input()
"""
find power of a number in a efficient method
"""

