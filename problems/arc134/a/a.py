#!/usr/bin/env python
N, L, W = map(int, input().split())
aN = [int(x) for x in input().split()] + [L]
ans, now = 0, 0
for a in aN:
    if(a > now):
        ans += (a - now + W - 1)//W
    now = a + W

print(ans)
