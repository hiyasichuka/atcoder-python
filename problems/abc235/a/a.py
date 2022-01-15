#!/usr/bin/env python
abc = int(input())

x = [int(a) for a in str(abc)]

a = x[0]
b = x[1]
c = x[2]

print(a*100+b*10+c + b*100 + c*10 + a + c*100 + a*10 +b)