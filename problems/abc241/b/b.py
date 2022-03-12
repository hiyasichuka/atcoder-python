#!/usr/bin/env python
N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
flg = True
for i in B:
    try:
        n = A.index(i)
        A.pop(n)
    except:
        print("No")
        flg = False
        break

if(flg):
    print("Yes")
