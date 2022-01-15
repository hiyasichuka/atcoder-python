a, n = map(int, input().split())
 
def abc235(x, a, cnt, items):
  if (x == 1):
    print(cnt)
    exit()
  if (x % a == 0):
    abc235(x//a, a, cnt+1, items)
    
  tmp = str(x)
  if (len(tmp) > 1) and (x % 10 != 0):
    tmp = tmp[1:] + tmp[0]
    if (int(tmp) not in items):
      items.add(int(tmp))
      abc235(int(tmp), a, cnt+1, items)
 
item = set([])
abc235(n, a, 0, item)
print(-1)