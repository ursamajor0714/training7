a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
print(f"{a+2} {b-2} {c*2} {d/2} {e//2} {f%2} {g**2}")



list1 = [int(input()) for _ in range(7)]
sign=("+2","-2","*2","/2","//2","%2","**2")
results = []
for i in range(7):
    expression = f"{list1[i]}{sign[i]}"
    results.append(eval(expression))
print(*results)


list1 = [int(input()) for _ in range(7)]
sign = ("+2", "-2", "*2", "/2", "//2", "%2", "**2")
results = []
i = 0 
while i < 7:
    expression = f"{list1[i]}{sign[i]}"
    results.append(eval(expression))
    i += 1
print(*results)









list1 = []
count = 0
while count < 7:
    a = int(input())
    b.append(a)
    count += 1
sign = ("+2", "-2", "*2", "/2", "//2", "%2", "**2")
results = []
i = 0 
while i < 7:
    expression = f"{b[i]}{sign[i]}"
    results.append(eval(expression))
    i += 1
print(*results)