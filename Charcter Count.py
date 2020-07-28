def char_count(string: str) -> dict:
    count: dict = {}
    for item in string:
        count[item] = string.count(item)
    return count


if __name__ == "__main__":
    string: str = str(input("String : "))
    count: dict = char_count(string=string)
    for item in count.keys():
        print(f"'{item}' : {count[item]}")
