#!/usr/bin/env python
L,R=map(int,input().split())
S = input()

L -= 1
R -= 1

ans = S[:L]+S[L:R+1][::-1]+S[R+1:]
print(ans)