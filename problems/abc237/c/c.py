S = input()
T = S.rstrip('a')
U = T.lstrip('a')

if U == U[::-1] and len(T) - len(U) <= len(S) - len(T):
    print("Yes")
else:
    print("No")
