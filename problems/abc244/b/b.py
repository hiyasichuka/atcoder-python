#!/usr/bin/env python

import numpy as np

a = int(input())
T = list(input())

e = np.array([1, 0])
s = np.array([0, -1])
w = np.array([-1, 0])
n = np.array([0, 1])

st = np.array([0, 0])
r = e
for t in T:
    if(t == "R" and (r == e).all()):
        r = s
    elif(t == "R" and (r == s).all()):
        r = w
    elif(t == "R" and (r == w).all()):
        r = n
    elif(t == "R" and (r == n).all()):
        r = e
    elif(t == "S"):
        st = st + r

print(str(st[0])+" "+str(st[1]))
