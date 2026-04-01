# T=int(input())

# for _ in range (T):
#     S,E=input().split()
#     S=int(S)

#     for i in E:
#         for _ in range(T):
#             print(i,end="")
#     print()





T = int(input())
results = []

for _ in range(T):
    S, E = input().split()
    S = int(S)
    
    line = ""
    for i in E:
        line += i * S
    
    results.append(line)

for res in results:
    print(res)