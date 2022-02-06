#!/usr/bin/env python
n = int(input())

mod = 998244353

'''
1桁 - 1けため
2桁 - n - 9
3桁 - n - 99
'''

ans = 0
for i in range(len(str(n)) - 1):
    i += 1
    mn = 10 ** (i - 1)
    mx = 10 ** i - 1
    cnt = mx - mn + 1
    ans += (mx + mn) * cnt // 2 % mod
    ans -= (mn - 1) * cnt
    ans %= mod

mn = 10 ** (len(str(n)) - 1)
mx = n
cnt = mx - mn + 1
ans += (mx + mn) * cnt // 2 % mod
ans -= (mn - 1) * cnt

print(ans % mod)
