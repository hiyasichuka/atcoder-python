#!/usr/bin/env python
import collections
N=int(input())
a = list(map(int,input().split()))

cc = collections.Counter(a)

print(cc.most_common()[-1][0])