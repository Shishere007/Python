def exp( number, power):
    ans = 1
    for num in range(power) :
        ans *= number
    return ans



number = int(input("Number : "))
power = int(input("power : "))
print (f"Ans : {exp(number,power)}")

_ = input()