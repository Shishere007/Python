# dynamic programming
fib_dic = {
    1: 0,
    2: 1,
    3: 1,
}


def fib_at(pos: int) -> dict:
    if pos in fib_dic.keys():
        return fib_dic[pos]
    fib_dic[pos] = fib_at(pos - 1) + fib_at(pos - 2)
    return fib_dic[pos]


pos = 1000
# for pos in range(1,1000) :
print(fib_at(pos))

# print(fib_dic)

_ = input()
