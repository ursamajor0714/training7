list1 = [int(input()) for _ in range(7)]
sign=("+2","-2","*2","/2","//2","%2","**2")

results = []
for i in range(7):
    expression = f"{list1[i]}{sign[i]}"
    results.append(eval(expression))
 print(*results)

print(*(eval(f"{list1[i]}{sign[i]}")for i in range(7)))