#!/usr/bin/env python
import itertools
import math

N, X = map(int, input().split())
li = []
cnt = 0

for i in range(N):
    raw = list(map(int, input().split()))
    raw.pop(0)
    li.append(raw)

for i in list(itertools.product(*li)):
    if math.prod(i) == X:
        cnt += 1

print(cnt)
