a,b,c,d,=[int(x)for _ in range(2) for x in input().split()]
E = c>a
F = d>b
G = E and F
print(G)