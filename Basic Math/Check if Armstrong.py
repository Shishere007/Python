def is_armstrong(number: int) -> bool:
    digit_count: int = len(str(number))
    sum: int = 0
    for num in str(number):
        sum += pow(int(num), digit_count)
    return number == sum


if __name__ == "__main__":
    number: int = 153
    if is_armstrong(number):
        print("Armstrong number")
    else:
        print("Not Armstrong number")

