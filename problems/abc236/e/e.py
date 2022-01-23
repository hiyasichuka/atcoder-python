n,*A = map(int,open(0).read().split())
ok,ng = 0,10**9+1
for _ in range(100):
    x = (ok+ng)/2
    s,t = 0,0
    for a in A:
        s,t = t,max(s,t)+(a-x)
    if max(s,t) >= 0:
        ok = x
    else:
        ng = x
print(ok)
ok,ng = 0,10**9+1
while ng-ok > 1:
    x = (ng+ok)//2
    s,t = 0,0
    for a in A:
        s,t = t,max(s,t)+(2*(a>=x)-1)
    if max(s,t) >= 1:
        ok = x
    else:
        ng = x
print(ok)