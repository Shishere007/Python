def is_armstrong(number: int) -> bool:
    digit_count: int = len(str(number))
    sum: int = 0
    for num in str(number):
        sum += pow(int(num), digit_count)
    return number == sum


if __name__ == "__main__":
    start: int = 1
    end: int = 10000
    for item in range(start, end + 1):
        if is_armstrong(number=item):
            print(item)

