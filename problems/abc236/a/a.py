#!/usr/bin/env python
s = list(input())
a,b=map(int,input().split())

swp = s[a-1]
swp2 = s[b-1]
s[a-1] = swp2
s[b-1] = swp

print("".join(s))

