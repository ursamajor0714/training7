# class Z:
#     def __init__(self):
#         self.hap=[]
#         self.hap1=[]

#     def X(self,n):
#         for i in range(n):
#             a,b=map(int, input().split())
#             self.hap.append((a,b))

#         c,d=map(int, input().split())

#         for i in range(n):
#             if self.hap[i][0]>=c and self.hap[i][1]<=d :
#                 self.hap1.append(self.hap[i])
        
#         for i in self.hap1:
#             print(i[0],i[1])

# n = int(input())
# J = Z()
# J.X(n)



# from re import A


# class S:
#     def A(self):
#         n=int(input())
#         a=[]
#         b=[]
#         for i in range(n):
#             c,d=map(int,input().split())
#             a.append(c)
#             b.append(d)
#         e,f=map(int,input().split())
#         for i in range(n):
#             if a[i]>= e and b[i] <=f:
#                 print(a[i],b[i])

# Q=S()
# Q.A()


# list1=list(map(int, [input() for _ in range(30)]))
# for i in list1:
#     print(i[0],end=" ")

# A=['a' , 'b' , 'c' , 'd' , 'e']
# print(f"['a' 'b' 'c' 'd' 'e']")
# for i in reversed(A):
#     print(i,end=" ")



# from itertools import combinations

# shorts = [int(input()) for _ in range(9)]
# target = 100

# for combo in combinations(shorts, 7):
#     if sum(combo) == target:
#         for height in sorted(combo):
#             print(height)
#         break



# shorts=[int(input()) for _ in range(9)]
# total=sum(shorts)
# gap=total-100

# for i in range(9):
#     for j in range(i+1,9):
#         if shorts[i] + shorts[j] == gap:
#             a,b=shorts[i],shorts[j]

#             shorts.remove(a)
#             shorts.remove(b)

#             for height in sorted(shorts):
#                 print(height)
#             exit()


# list1=list(input())

# dap=list1[0::2]
# print(*dap)


# list1=list(input())
# print("".join(reversed(list1)))


# a,b=map(int, input().split())
# hap=[]
# for i in range(a,b+1):
#     if i%2==0:
#         hap.append(i)
# print(sum(hap))

# hap=[]
# while True:
#     a=int(input())
#     if a==0:
#         break
#     hap.append(a)

# print("cnt =",len(hap))
# print("sum =",sum(hap))


# hap=[]
# while True:
#     a=int(input())
#     if a<1 or a>5 :
#         break

#     if a%2==0:
#         hap.append(a)
    
# print(int(sum(hap)/ len(hap)))



# list1=[int(input()) for _ in range(28)]

# for i in range(1,31):
#     if i not in list1:
#         print(i)

#3052 백준준
list1=[int(input()) for _ in range(10)]
hap=[]
for i in list1:
    hap.append(i%42)
