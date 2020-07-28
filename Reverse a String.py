def reverse_string(string: str) -> str:
    return "".join(list(string)[::-1])


def reverse_string_2(string: str) -> str:
    return string[::-1]


string = "string"
print(reverse_string(string))
print(reverse_string_2(string))

