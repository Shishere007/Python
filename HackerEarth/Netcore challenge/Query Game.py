def query_game (N, A, Q, P):
    ret = []
    for q in P:
        if q[0] ==  1:
            A.reverse()
        elif q[0] == 2:
            A[q[1]-1],A[q[2]-1] = A[q[2]-1],A[q[1]-1]
        elif q[0] == 3:
            ret.append(A.index(q[1])+1)
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    P = [list(map(int, input().split())) for i in range(Q)]

    out_ = query_game(N, A, Q, P)
    print (' '.join(map(str, out_)))