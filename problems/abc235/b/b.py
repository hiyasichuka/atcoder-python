#!/usr/bin/env python
N = int(input())
h = list(map(int,input().split()))

tmp = h[0]
for i in range(N-1):
  if (h[i+1] > tmp):
    tmp = h[i+1]
  else:
    break
    

print(tmp)
