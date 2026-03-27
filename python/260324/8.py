a, b = map(int, input().split())

print(f"{a} / {b} = {a//b} ... {a%b}")



list=list(input().split())
a=int(list[0])
b=int(list[1])
c=int(list[2])
ever=int(len(list))
print(f"sum = {a+b+c}")
print(f"avg = {int(a+b+c)/ever}")