# a=int(input())
# b=int(input())
# hap=[]
# for i in range(b,a+1):
#     hap.append(i**2)

# print(*sorted(hap))

# class Z:
#     def __init__(self):
#         self.Q=[]
#         self.Y=[]
#     def X(self, n):
#         for i in range(n):
#             a,b = map(int,input().split())
#             self.Y.append((a, b))

#         c,d= map(int,input().split())

#         if (a>=c) and (b<=d):
#             self.Q.append((a, b))

#         for i in self.Q:
#             print(i[0],i[1])



# n=int(input())
# H=Z()
# H.X(n)

# class Z:
#     def __init__(self):
#         self.hap=[]
#         self.hap1=[]
#         self.hap2=[]
#     def X(self, n):
#         for i in range(n):
#             a,b = map(int,input().split())
#             self.hap.append((a,b))
        
#         c,d = map(int,input().split())
#         self.hap1.append((c,d))

#         for i in range(n):
#             if self.hap[i][0] > self.hap1[0][0] and self.hap[i][1] > self.hap1[0][1]:
#                 self.hap2.append(self.hap[i])

#         print(self.hap2)

# n=int(input())
# J=Z()
# J.X(n)


class Z:
    def __init__(self):
        self.hap = []
        self.hap2 = []

    def X(self, n):
        for i in range(n):
            a, b = map(int, input().split())
            self.hap.append((a, b))
        
        y, p = map(int, input().split())

        for i in range(n):
            if self.hap[i][0] >= y and self.hap[i][1] <= p:
                self.hap2.append(self.hap[i])
        
        for res in self.hap2:
            print(res[0], res[1])

n = int(input())
J = Z()
J.X(n)