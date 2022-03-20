#!/usr/bin/env python
n = int(input())

cards = list(range(1, 2*n+1+1))

while (True):
    ans = cards.pop()
    print(ans, flush=True)
    if(len(cards) == 0):
        break
    aoki = int(input())
    cards.remove(aoki)
