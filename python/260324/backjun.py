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

# A=list(input().split())
# print("/".join(A))





# a=int(input())
# b=a*2-1

# for i in range(1,b+1,2):
#     print(((b - i) // 2) * " " + "*" * i)
# for i in range(b-2,-1,-2):
#     print(((b - i) // 2) * " " + "*" * i)



# A=input()
# B=A[::-1]

# if A == B :
#     print(1)
# else:
#     print(0)

# A=list(input())
# B=max(A, key=A.count)
# C=[B]
# if B>1:
#     print("?")
#     if B :
#         print(B)


# A=input().upper()
# U=list(set(A))

# C=[]

# for x in U:
#     C.append(A.count(x))

# if C.count(max(C))> 1:
#     print("?")
# else:
#     max_index = C.index(max(C))
#     print(U[max_index])

# N=int(input())
# hap=[]

# for i in range(N):
#     RGB=list(map(int, input().split()))
#     hap.append(RGB)
# print(hap)





# import sys

# # 1. 입력 받기
# N = int(sys.stdin.readline())
# cost = []
# for _ in range(N):
#     cost.append(list(map(int, sys.stdin.readline().split())))

# # 2. 두 번째 줄부터 마지막 줄까지 누적합 계산 (DP)
# for i in range(1, N):
#     # 현재 빨강(0) = 현재 빨강 + min(이전 초록, 이전 파랑)
#     cost[i][0] += min(cost[i-1][1], cost[i-1][2])
#     # 현재 초록(1) = 현재 초록 + min(이전 빨강, 이전 파랑)
#     cost[i][1] += min(cost[i-1][0], cost[i-1][2])
#     # 현재 파랑(2) = 현재 파랑 + min(이전 빨강, 이전 초록)
#     cost[i][2] += min(cost[i-1][0], cost[i-1][1])

# # 3. 마지막 줄의 세 값 중 최솟값이 최종 정답
# print(min(cost[N-1]))


# hap=[]
# for i in range(5):
#     i=input()
#     hap.append(i)
# print(hap)


# hap=[]
# for i in range(5):
#     i=input()
#     hap.append(i)
# print(f"[{", ".join(hap)}]")
# print(" ".join(hap))


# hap=[1,2,3,4,5]
# print(f"last: {hap[4]}")
# hap.remove(hap[4])
# print(hap)
# print(f"len: {len(hap)}")
# print()
# print(f"second: {hap[1]}")
# hap.remove(hap[1])
# print(hap)
# print(f"len: {len(hap)}")

# hap=[]
# for i in range(5):
#     i=input()
#     hap.append(i)
# print(f"[{", ".join(hap)}]")
# del hap[3:5]
# print(f"[{", ".join(hap)}]")

# hap=[]
# for i in range(5):
#     i=int(input())
#     hap.append(i)
# print(hap[4] + hap[3])

# A = ['a', 'b', 'c', 'd', 'e']
# print(A)
# print(A[0]+A[2]+A[-1])

# A=[]

# for i in range(5):
#     i=input()
#     A.append(i)
# B=A.copy()
# C=A[::-1]
# print(f"[{", ".join(C)}]")
# for i in range(3):
#     i=input()
#     B.append(i)
# print(f"[{", ".join(B)}]")
# print(f"[{", ".join(A)}]")


 