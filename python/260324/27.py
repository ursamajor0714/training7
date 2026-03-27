    E = int(input())
F = int(input())
G = ["+", "-", "*", "/", "//", "%", "**"]

for i in range(7):
    print(E, G[i], F, "=", eval(f"{E} {G[i]} {F}"))