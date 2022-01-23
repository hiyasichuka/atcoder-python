from sys import setrecursionlimit
setrecursionlimit(10 ** 7)
 
n = int(input())
a = [list(map(int, input().split())) for _ in range(2 * n - 1)]
 
used = [True] * (2 * n)
 
ans = 0
 
def func(val, now):
    if now == 2 * n:
        global ans
        ans = max(ans, val)
        return 
    if not used[now]:
        func(val, now+1)
        return 
    
    used[now] = False
    for i in range(2*n-1-now):
        if used[i+now+1]:
            used[i+now+1] = False
            func(val ^ a[now][i], now+1)
            used[i+now+1] = True
    used[now] = True
 
func(0, 0)
print(ans)