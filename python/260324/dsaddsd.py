#a=input()
#b = input()
#sign=["+","-","*","/","//","%","**"]
#i = 0;
#while(i < len(sign)):
#    hap=f"{a} {sign[i]} {b}"
#    result=eval(hap)
#    print(f"{hap} = {result})")
#    i = i + 1
E = int(input())
F = int(input())
G = ["+", "-", "*", "/", "//", "%", "**"]

for i in range(7):
    print(E, G[i], F, "=", eval(f"{E} {G[i]} {F}"))