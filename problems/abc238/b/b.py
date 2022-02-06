N =int(input())
A = list(map(int,input().split()))
 
cut = [0]
a = A[0]
cut.append(a)
for i in range(1,N):
  a = A[i] + a
  if a >= 360:
    a -= 360
  cut.append(a)
cut = sorted(cut)
 
p = []
for j in range(len(cut)-1):
  p.append(cut[j+1]-cut[j])
p.append(360-cut[-1])
 
print(max(p))