# # T=int(input())

# # for _ in range (T):
# #     S,E=input().split()
# #     S=int(S)

# #     for i in E:
# #         for _ in range(T):
# #             print(i,end="")
# #     print()





# T = int(input())
# results = []

# for _ in range(T):
#     S, E = input().split()
#     S = int(S)
    
#     line = ""
#     for i in E:
#         line += i * S
    
#     results.append(line)

# for res in results:
#     print(res)


# a = input()
# b = input()

# print("Capital of",a,"is",b)



# class world:
#     def __init__(self,con,cap):
#         self.com=con
#         self.cap=cap
#     def print(self):
#         print(f"Capital of {self.com} is {self.cap}")

# con,cap=[input() for _ in range(2)]
# world=world(con,cap)
# world.print()

#정올 레벨테스트 1번
# a,b,c=[(input())for _ in range(3)]
# a=float(a)
# b=float(b)
# print(f"{round(a,2):.2f}" )
# print(f"{round(b,2):.2f}" )
# print(c)


# total=int(input())
# out=[]

# for i in range(total):
#     i=list(map(int,input().split()))
#     gen,age,pa=i[0],i[1],i[2]
    
#     is_qualified = True

#     if gen !=1 :
#         is_qualified = False
#     elif age < 19 or age >40:
#         is_qualified = False
#     elif age <= 18 and pa == 0 :
#         is_qualified = False
#     if not is_qualified:
#         out.append(i)

# print(len(out))
# print(out)

# N=int(input())
# hap=[]

# for i in range(N):
#     i=list(map(int, input().split()))
#     hap.append(i)

# hap0=[item[0] for item in hap]
# goodred=min(hap0)

# hap1=[item[1] for item in hap]
# goodgreed=min(hap1)

# hap2=[item[2] for item in hap]
# goodblur=min(hap2)

# print(goodred+goodgreed+goodblur)



# pi=3.14
# a=int(input())
# print(f"PI = {pi}")
# print(f"Area = {a} * {a} * {pi} = {a * a * pi:.1f}")

# A=[]

# for i in range(3):
#     i=input()
#     A.append(i)

# print("-".join(A))

A=list(input().split())
print("/".join(A))