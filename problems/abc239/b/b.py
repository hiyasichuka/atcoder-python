#!/usr/bin/env python
a = int(input())
s = str(a)

if(a >= 0):
    if (len(s) == 1):
        atama = 0
        print(atama)
    else:
        atama = int(s[0:len(s)-1])
        print(atama)
else:
    if (len(s) == 2):
        atama = -1
        print(atama)
    else:
        atama = int(s[0:len(s)-1])
        ketsu = int(s[-1])
        if(ketsu == 0):
            print(atama)
        else:
            print(atama-1)
