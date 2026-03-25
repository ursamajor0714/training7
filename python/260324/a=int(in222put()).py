a=int(input())
b=int(input())
print(eval(f"{a}-10 ,"+", {b}*2 ,"=", {int(a+b)}"))