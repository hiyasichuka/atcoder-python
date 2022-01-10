import heapq
N, K = map(int, input().split())
P = list(map(int, input().split()))
s = P[:K]
heapq.heapify(s)
print(min(s))
for i in range(K, N):
  heapq.heappush(s, P[i])
  heapq.heappop(s)
  print(s[0])