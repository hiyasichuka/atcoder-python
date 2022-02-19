#!/usr/bin/env python
x1, y1, x2, y2 = map(int, input().split())

# (x1-x2)^2+(y1-y2)^2の値が2,10,16,18,20

ans = (x1-x2)**2 + (y1-y2)**2

if(ans == 2 or ans == 4 or ans == 10 or ans == 16 or ans == 18 or ans == 20):
    print("Yes")
else:
    print("No")
