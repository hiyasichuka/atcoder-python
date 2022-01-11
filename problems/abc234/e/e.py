#!/usr/bin/env python
x=input()
l=len(x)
r=range
for i in r(10):
  for d in r(-9,9):
    if 0<=i+d*~-l<=9 and (a:=''.join([str(i+d*j) for j in r(l)]))>=x: exit(print(a))