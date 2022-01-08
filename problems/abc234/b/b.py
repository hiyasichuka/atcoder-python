#!/usr/bin/env python
import math
# nの値を取得
n = int(input())
# 座標はx座標はx、y座標はyと分けてリストに
x = list(range(n))
y = list(range(n))
for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
for j in range(n):
    for t in range(n):
        if math.sqrt(pow(x[t]-x[j], 2) + pow(y[t] - y[j], 2)) > ans:
            ans = math.sqrt(pow(x[t]-x[j], 2) + pow(y[t] - y[j], 2))
print(round(ans, 10))
