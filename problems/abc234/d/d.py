N, K = map(int, input().split())
P = list(map(int, input().split()))

_P = P[:K]
sortedP = sorted(_P, reverse=True)
ans = sortedP[K-1]

for i in range(N-K+1):
    _P.append(P[K+i])
    Pi = _P[-1]
    if (Pi > ans):
        sortedP[K]
    print(ans)
