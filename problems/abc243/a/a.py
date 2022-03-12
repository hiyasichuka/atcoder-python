#!/usr/bin/env python
v, a, b, c = map(int, input().split())

diff = v

while True:
    diff = diff - a
    if(diff < 0):
        print("F")
        break

    diff = diff - b

    if(diff < 0):
        print("M")
        break

    diff = diff - c

    if(diff < 0):
        print("T")
        break
