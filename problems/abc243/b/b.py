#!/usr/bin/env python
n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [x-y for (x, y) in zip(A, B)]

ans1 = C.count(0)
print(ans1)

cnt = 0
for i in A:
    if(i in set(B)):
        cnt = cnt+1

print(cnt-ans1)
