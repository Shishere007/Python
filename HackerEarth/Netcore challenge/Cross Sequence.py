import itertools

# def solve (N, A, K):
#     pos = K-N-1
#     if pos < 0:
#         return 0
#     res = {}
#     for (a,b) in itertools.combinations(A,2):
#         ans = abs(a-b)
#         if ans in res:
#             res[ans] += 1
#         else:
#             res[ans] = 1
#     curr = 0
#     for key,val in [(key,res[key]) for key in sorted(res)]:
#         curr += (val*2)
#         if pos <= curr:
#             return key

# def solve (N, A, K):
#     if K-1 <= N:
#         return 0
#     res = {}
#     for (a,b) in itertools.permutations(A,2):
#         ans = abs(a-b)
#         if ans in res:
#             res[ans] += 1
#         else:
#             res[ans] = 1
#     curr = 0
#     pos = K - N - 1
#     for key in sorted(res):
#         curr += (res[key])
#         if pos <= curr:
#             return key

# def solve (N, A, K):
#     if K-1 <= N:
#         return 0
#     res = []
#     for perm in itertools.permutations(A,2):
#         res.append(abs(perm[0] - perm[1]))
#     return sorted(res)[K-N-1]

# def solve (N, A, K):
#     res = []
#     for a in A:
#         for b in A:
#             res.append(abs(a - b))
#     return sorted(res)[K-1]

def solve (N, A, K):
    if K-1 <= N:
        return 0
    res = {}
    for a in A:
        for b in A:
            ans = abs(a-b)
            if ans in res:
                res[ans] += 1
            else:
                res[ans] = 1
    curr = 0
    for a in sorted(res):
        curr += (res[a])
        if K-1 < curr:
            return a

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = solve(N, A, K)
    print (out_)
