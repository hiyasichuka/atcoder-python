#!/usr/bin/env python
from collections import defaultdict
N,Q=map(int,input().split())
a = list(map(int,input().split()))
dic = defaultdict(list)

for i in range(N):
  dic[a[i]].append(i+1)

for _ in range(Q):
  target,num = map(int,input().split())
  if len(dic[target]) < num:
    print(-1)
  else:
    print(dic[target][num-1])
  