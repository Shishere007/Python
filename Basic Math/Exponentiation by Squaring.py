def exp( number, power):
    if ( power == 1 ):
        return number  
    if ( power % 2 == 0 ):
        return exp( number * number, power // 2 )
    return number * exp( number * number, power // 2 )
number = 2
power = 5
print (exp(number,power))


"""
find power of a number in a efficient method
"""