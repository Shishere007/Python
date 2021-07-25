import itertools
def MaxPairs (N, nums):
    score_list = []
    combinations = itertools.combinations(enumerate(nums),2)
    for comb in combinations:
        a = comb[0]
        b = comb[1]
        x = a[1] | b[1]
        x &= -x
        score_list.append((x,set((a[0],b[0]))))
    score_list = sorted(score_list,reverse=True,key=lambda y:y[0])
    cnt = 1
    score = score_list[0][0]
    ind = 1
    while (cnt != N/2):
        if not (score_list[ind-1][1] & score_list[ind][1]):
            score += score_list[ind][0]
            cnt += 1
        ind += 1
    return score

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    out_ = MaxPairs(N, nums)
    print (out_)
