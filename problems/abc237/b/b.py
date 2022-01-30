#!/usr/bin/env python
H, W = map(int, input().split())
matrix = []
for i in range(H):
    matrix.append([int(x) for x in input().split()])
for row in zip(*matrix):
    print(" ".join(map(str, row)))
