N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(K):
    a = ans % N 
    ans += A[a]

print(ans)
