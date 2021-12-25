#!/usr/bin/env python
X, Y = map(int, input().split())

s = Y - X

if (s > 0):
  print(-(-s // 10))
else:
  print(0)
